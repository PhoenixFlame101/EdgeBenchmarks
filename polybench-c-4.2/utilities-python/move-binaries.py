#!/usr/bin/env python3

import os
import subprocess
import sys

TARGET_DIR = "."
DESTINATION_DIR = sys.argv[1]

# -p is to avoid "File Exists" errors
subprocess.run(f"mkdir -p {DESTINATION_DIR}", shell=True)

categories = [
    'linear-algebra/blas',
    'linear-algebra/kernels',
    'linear-algebra/solvers',
    'datamining',
    'stencils',
    'medley'
]

for cat in categories:
    target = os.path.join(TARGET_DIR, cat)
    if not os.path.isdir(target):
        print(f"directory {target} not found.")
        sys.exit(1)

    try:
        dirs = os.listdir(target)
    except OSError:
        print(f"Error reading directory {target}.")
        sys.exit(1)

    for dir in dirs:
        dir_path = os.path.join(target, dir)
        # Skip hidden files and non-directories
        if dir.startswith('.') or not os.path.isdir(dir_path):
            continue

        kernel = dir
        target_dir = dir_path

        command = f"mv {target_dir}/{kernel} {DESTINATION_DIR}"
        print(command)
        subprocess.run(command, shell=True)
