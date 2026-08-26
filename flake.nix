{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    dottyp.url = "github:luiswirth/dottyp";
    dottyp.inputs.nixpkgs.follows = "nixpkgs";

    treefmt-nix.url = "github:numtide/treefmt-nix";
    treefmt-nix.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = {
    nixpkgs,
    dottyp,
    treefmt-nix,
    ...
  }: let
    forEachSystem = f:
      nixpkgs.lib.genAttrs ["aarch64-darwin" "x86_64-linux"]
      (system: f nixpkgs.legacyPackages.${system});

    # One environment, entered by the shell and by the checks alike.
    tools = pkgs: with pkgs; [typst tinymist just];

    packagePath = "${dottyp}/pkg";
  in {
    # Typst is deliberately absent: a formatter there would undo the semantic
    # line breaks a document is written in.
    formatter = forEachSystem (pkgs:
      treefmt-nix.lib.mkWrapper pkgs {
        projectRootFile = "flake.nix";
        programs.alejandra.enable = true;
        programs.just.enable = true;
      });

    devShells = forEachSystem (pkgs: {
      default = pkgs.mkShell {
        packages = tools pkgs;
        TYPST_PACKAGE_PATH = packagePath;
      };
    });
  };
}
