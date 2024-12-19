#!/usr/bin/env python3

import os
import sys
import subprocess

# Visits every directory, calls make, and then executes the benchmark
# (Designed for making sure every kernel compiles/runs after modifications)
#
# usage python3 run-all.py target-dir [output-file]

WARMPUPS = 3
RUNS = 15

TARGET_DIR = "."
START_FROM = ""
TARGET_BENCH = ""
BUILD_ONLY = False
RUN_ONLY = False
IS_NATIVE = True
IS_WASM = False
IS_DOCKER = False
OUTFILE = ""

if "-f" in sys.argv:
    START_FROM = sys.argv[sys.argv.index('-f')+1]
if "-t" in sys.argv:
    TARGET_BENCH = sys.argv[sys.argv.index('-t')+1]
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
elif "-a" in sys.argv or "--all" in sys.argv:
    IS_WASM = True
    IS_DOCKER = True

# Remove command flags
sys.argv = [item for item in sys.argv if not item.startswith('-')]

# if len(sys.argv) >= 2:
#     TARGET_DIR = sys.argv[1]

# if len(sys.argv) == 3:
#     OUTFILE = sys.argv[2]

categories = [
    'datamining',
    'linear-algebra/blas',
    'linear-algebra/kernels',
    'linear-algebra/solvers',
    'medley',
    'stencils'
]

if OUTFILE:
    outfile = open(OUTFILE, 'w')
else:
    outfile = sys.stdout

started = not START_FROM
for cat in categories:
    target = os.path.join(TARGET_DIR, cat)
    if not os.path.isdir(target):
        print(f"directory {target} not found.", file=outfile)
        sys.exit(1)

    try:
        dirs = sorted(os.listdir(target))
    except OSError:
        print(f"Error reading directory {target}.", file=outfile)
        sys.exit(1)

    for dir in dirs:
        if START_FROM == dir:
            started = True
        if not started:
            continue

        if TARGET_BENCH and dir != TARGET_BENCH:
            continue

        dir_path = os.path.join(target, dir)
        # Skip hidden files and non-directories
        if dir.startswith('.') or not os.path.isdir(dir_path):
            continue

        kernel = dir
        target_dir = dir_path

        if not RUN_ONLY:
            make_command = f"cd {target_dir} && make"
            print(make_command, file=outfile)
            subprocess.run(make_command, shell=True, stdout=outfile)

            make_command = f"cd {target_dir} && docker build . -t {kernel}"
            print(make_command, file=outfile)
            subprocess.run(make_command, shell=True, stdout=outfile)

        if not BUILD_ONLY:
            run_commands = []
            if IS_NATIVE:
                run_commands.append(f"{target_dir}/{kernel}")
                subdir = 'native'
                subprocess.run('mkdir -p benchmarks/polybench/native', shell=True)
            if IS_WASM:
                run_commands.append(f"wasmtime {target_dir}/{kernel}.wasm")
                subdir = 'wasm'
                subprocess.run('mkdir -p benchmarks/polybench/wasm', shell=True)
            if IS_DOCKER:
                run_commands.append(f"docker run --rm {kernel}")
                subdir = 'docker'
                subprocess.run('mkdir -p benchmarks/polybench/docker', shell=True)

            for i in range(sum((IS_NATIVE, IS_WASM, IS_DOCKER))):
                subprocess.run(f"hyperfine '{run_commands[i]}' --warmup {WARMPUPS} --runs {RUNS} --export-json benchmarks/polybench/{subdir}/{kernel}.json", shell=True)

outfile.close()
