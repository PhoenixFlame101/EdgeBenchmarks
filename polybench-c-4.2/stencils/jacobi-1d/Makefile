include ../../config.mk

EXTRA_FLAGS=

all: jacobi-1d jacobi-1d.wasm

jacobi-1d: jacobi-1d.c jacobi-1d.h
	$(VERBOSE) $(CC) -o jacobi-1d jacobi-1d.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

jacobi-1d.wasm: jacobi-1d.c jacobi-1d.h
	$(VERBOSE) $(CC_WASM) -o jacobi-1d.wasm jacobi-1d.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f jacobi-1d jacobi-1d.wasm
