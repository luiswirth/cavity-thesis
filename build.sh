#!/usr/bin/env sh

cd "$(dirname "$0")" || exit 1
typst compile src/main.typ out/thesis.pdf --root $(pwd)
