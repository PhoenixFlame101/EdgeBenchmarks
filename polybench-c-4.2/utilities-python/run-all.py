#!/usr/bin/env python3

import os
import sys
import subprocess

# Visits every directory, calls make, and then executes the benchmark
# (Designed for making sure every kernel compiles/runs after modifications)
#
# usage python3 run-all.py target-dir [output-file]

TARGET_DIR = "."
BUILD_ONLY = False
RUN_ONLY = False
IS_NATIVE = True
IS_WASM = False
IS_DOCKER = False
OUTFILE = ""

if "-b" in sys.argv or "--build" in sys.argv:
    BUILD_ONLY = True
if "-r" in sys.argv or "--run" in sys.argv:
    RUN_ONLY = True
if "-w" in sys.argv or "--wasm" in sys.argv:
    IS_WASM = True
    IS_NATIVE = False
elif "-d" in sys.argv or "--docker" in sys.argv:
    IS_DOCKER = True
    IS_NATIVE = False

# Remove command flags
sys.argv = [item for item in sys.argv if not item.startswith('-')]

if len(sys.argv) >= 2:
    TARGET_DIR = sys.argv[1]

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

        if not RUN_ONLY:
            if IS_NATIVE or IS_WASM:
                make_command = f"cd {target_dir} && make"
            elif IS_DOCKER:
                make_command = f"cd {target_dir} && docker build . -t {kernel}"
            print(make_command, file=outfile)
            subprocess.run(make_command, shell=True, stdout=outfile)

        if not BUILD_ONLY:
            cd_command = f"cd {target_dir}"
            subprocess.run(cd_command, shell=True)
            if IS_NATIVE:
                run_command = f"./{kernel}"
            if IS_WASM:
                run_command = f"wasmtime {kernel}.wasm"
            elif IS_DOCKER:
                run_command = f"docker run --rm {kernel}"

            subprocess.run('mkdir -p benchmarks', shell=True)
            subprocess.run(f"hyperfine '{
                           run_command}' --export-json benchmarks/{kernel}.json", shell=True)

outfile.close()
