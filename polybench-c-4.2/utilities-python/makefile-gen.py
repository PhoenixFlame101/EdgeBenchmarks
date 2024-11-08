#!/usr/bin/env python3

import os
import sys

# Generates Makefile for each benchmark in polybench
# Expects to be executed from root folder of polybench
# NOTE: -cfg flag is enable by default

GEN_CONFIG = True
TARGET_DIR = "."

for arg in sys.argv[1:]:
    if arg == "--no-cfg":
        GEN_CONFIG = False
    else:
        TARGET_DIR = arg

categories = {
    'linear-algebra/blas': 3,
    'linear-algebra/kernels': 3,
    'linear-algebra/solvers': 3,
    'datamining': 2,
    'stencils': 2,
    'medley': 2
}

extra_flags = {
    'cholesky': '-lm',
    'gramschmidt': '-lm',
    'correlation': '-lm'
}

# Process each category
for key, depth in categories.items():
    target = os.path.join(TARGET_DIR, key)

    if not os.path.isdir(target):
        print(f"Directory {target} not found.")
        sys.exit(1)

    for dir in os.listdir(target):
        dir_path = os.path.join(target, dir)

        # Skip hidden files and non-directories
        if dir.startswith('.') or not os.path.isdir(dir_path):
            continue

        kernel = dir
        makefile_path = os.path.join(dir_path, 'Makefile')
        polybench_root = '../' * depth
        config_file = os.path.join(polybench_root, 'config.mk')
        utility_dir = os.path.join(polybench_root, 'utilities')

        with open(makefile_path, 'w') as file:
            file.write(f"""include {config_file}

EXTRA_FLAGS={extra_flags.get(kernel, '')}

{kernel}: {kernel}.c {kernel}.h
\t$(VERBOSE) $(CC) -o {kernel} {kernel}.c $(CFLAGS) -I. -I{utility_dir} {utility_dir}/polybench.c $(EXTRA_FLAGS)

clean:
\t@ rm -f {kernel}
""")

# Generate config.mk file if needed
if GEN_CONFIG:
    config_path = os.path.join(TARGET_DIR, 'config.mk')
    with open(config_path, 'w') as file:
        file.write("""CC=gcc
CFLAGS=-O3 -DPOLYBENCH_TIME -DPOLYBENCH_USE_C99_PROTO
""")
