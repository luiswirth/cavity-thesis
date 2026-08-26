# Compile the document to out/.
build:
    mkdir -p out
    typst compile src/main.typ out/thesis.pdf --root "$PWD"

# Recompile it on every change.
watch:
    mkdir -p out
    typst watch src/main.typ out/thesis.pdf --root "$PWD"

# Check that the document still compiles, keeping nothing.
ci:
    nix fmt -- --ci
    typst compile src/main.typ "$(mktemp -d)/thesis.pdf" --root "$PWD"
