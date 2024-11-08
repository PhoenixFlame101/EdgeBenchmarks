#!/usr/bin/env python3

import os
import sys
import subprocess
import time_benchmark

# Visits every directory, calls make, and then executes the benchmark
# (Designed for making sure every kernel compiles/runs after modifications)
#
# usage python3 run-all.py target-dir [output-file]

TARGET_DIR = "."

if len(sys.argv) >= 2:
    TARGET_DIR = sys.argv[1]

OUTFILE = ""
if len(sys.argv) == 3:
    OUTFILE = sys.argv[2]

categories = [
    'linear-algebra/blas',
    'linear-algebra/kernels',
    'linear-algebra/solvers',
    'datamining',
    'stencils',
    'medley'
]

if OUTFILE:
    outfile = open(OUTFILE, 'w')
else:
    outfile = sys.stdout

for cat in categories:
    target = os.path.join(TARGET_DIR, cat)
    if not os.path.isdir(target):
        print(f"directory {target} not found.", file=outfile)
        sys.exit(1)

    try:
        dirs = os.listdir(target)
    except OSError:
        print(f"Error reading directory {target}.", file=outfile)
        sys.exit(1)

    for dir in dirs:
        dir_path = os.path.join(target, dir)
        # Skip hidden files and non-directories
        if dir.startswith('.') or not os.path.isdir(dir_path):
            continue

        kernel = dir
        target_dir = dir_path

        make_command = f"cd {target_dir} && make clean && make"
        print(make_command, file=outfile)
        subprocess.run(make_command, shell=True, stdout=outfile)

        run_command = f"cd {target_dir} && ./{kernel}"
        time_benchmark.run_benchmark(run_command, outfile)

outfile.close()
