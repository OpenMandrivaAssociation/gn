#!/bin/sh
version=$(date +%Y%m%d)
# gn can't be built from a "git archive"-d tarball, must package .git
# (and even --depth 1 won't work)
git clone https://gn.googlesource.com/gn
tar cf gn-${version}.tar gn
zstd --ultra -22 --rm *.tar
