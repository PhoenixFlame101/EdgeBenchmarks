#!/usr/bin/env python3

import os
import sys
import subprocess

TARGET_DIR = "."

if 1 in range(len(sys.argv)):
    TARGET_DIR = sys.argv[1]

categories = [
    'linear-algebra/blas',
    'linear-algebra/kernels',
    'linear-algebra/solvers',
    'datamining',
    'stencils',
    'medley'
]

# Iterate over each category
for cat in categories:
    target = os.path.join(TARGET_DIR, cat)

    if not os.path.isdir(target):
        print(f"Directory {target} not found.")
        continue

    for dir_name in os.listdir(target):
        dir_path = os.path.join(target, dir_name)

        # Skip hidden files and non-directories
        if dir_name.startswith('.') or not os.path.isdir(dir_path):
            continue

        command = f"cd {dir_path} && make clean; rm -f Makefile; rm -f Dockerfile"
        print(command)
        subprocess.run(command, shell=True)
