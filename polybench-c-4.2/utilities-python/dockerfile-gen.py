#!/usr/bin/env python3

import sys
import os

# Generates Dockerfile for each benchmark in polybench
# Expects to be executed from root folder of polybench

categories = {
    'linear-algebra/blas': 3,
    'linear-algebra/kernels': 3,
    'linear-algebra/solvers': 3,
    'datamining': 2,
    'stencils': 2,
    'medley': 2
}

# Process each category
for key, depth in categories.items():
    target = os.path.join(os.getcwd(), key)

    if not os.path.isdir(target):
        print(f"Directory {target} not found.")
        sys.exit(1)

    for dir in os.listdir(target):
        dir_path = os.path.join(target, dir)

        # Skip hidden files and non-directories
        if dir.startswith('.') or not os.path.isdir(dir_path):
            continue

        kernel = dir
        dockerfile_path = os.path.join(dir_path, 'Dockerfile')
        polybench_root = '../' * depth

        with open(dockerfile_path, 'w') as file:
            file.write(f"""FROM ghcr.io/phoenixflame101/polybench@sha256:3a6e91717902dca33dd7d4023b811954b9e2937ea511b703a0da064c5174c5e8
# Remove all files except ./{kernel}
RUN find . ! -name '{kernel}' -type f -exec rm -f {{}} +
CMD ["./{kernel}"]
""")
