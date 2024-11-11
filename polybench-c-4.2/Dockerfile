# Stage 1: Build stage
FROM python@sha256:db1afbfdc089b792bed227d70e1b1607c16bacb391f1257b7af1f0e6b2384480 as build

# Copy build files
WORKDIR /polybench
COPY . /polybench

# Install clang deps and clang 18
RUN apt update && apt install -y software-properties-common lsb-release
RUN wget -qO- https://apt.llvm.org/llvm.sh | bash -s -- 18
RUN ln -s /usr/bin/clang-18 /usr/bin/clang

# Build all the polybench binaries and move them to /usr/bin/polybench
RUN chmod +x utilities-python/*
RUN utilities-python/makefile-gen.py
RUN utilities-python/run-all.py -b
RUN utilities-python/move-binaries.py /usr/bin/polybench

# -----------------------------

# Stage 2: Final image (Debian Slim)
FROM debian@sha256:36e591f228bb9b99348f584e83f16e012c33ba5cad44ef5981a1d7c0a93eca22

WORKDIR /polybench
# Move the binaries to the final image
COPY --from=build /usr/bin/polybench /polybench

CMD ["bash"]
