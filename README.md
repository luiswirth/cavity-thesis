# BEM Benchmark of the Ehrenpreis–Palamodov Gaussian Process for Maxwell Cavity Scattering

This repository contains the [Typst](https://typst.app/) source files for
the Semester Thesis of Luis Wirth under the supervision of Prof. Dr.-Ing. Stefan
Kurz, for Computational Science and Engineering (CSE) at ETH Zürich.

For the implementation itself, see
- [maxwellgp](https://github.com/luiswirth/maxwellgp), the Maxwell-constrained EPGP framework.
- [cavity-maxwellgp](https://github.com/luiswirth/cavity-maxwellgp), the cavity-specific EPGP solver built on maxwellgp.
- [cavity-bem](https://github.com/luiswirth/cavity-bem), the BEM reference solver for the PEC cavity.
- [cavity-benchmark](https://github.com/luiswirth/cavity-benchmark), the cross-validation and benchmarking harness.

## Building the thesis

The devShell carries Typst and the [dottyp](https://github.com/luiswirth/dottyp)
notation library the document imports, so `direnv allow` or `nix develop` is all
the setup there is.
- `just build` compiles `out/thesis.pdf`;
- `just watch` recompiles on save.
