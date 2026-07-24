#!/usr/bin/env sh

cd "$(dirname "$0")" || exit 1
typst watch src/main.typ out/thesis.pdf --root $(pwd)
