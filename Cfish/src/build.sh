#!/bin/bash
make build ARCH=x86-64-modern COMP=clang numa=no native=no \
    CFLAGS="-O3 -Wall -std=c11 -arch x86_64 -I. -DNDEBUG" \
    LDFLAGS="-arch x86_64 -lm -lpthread"
