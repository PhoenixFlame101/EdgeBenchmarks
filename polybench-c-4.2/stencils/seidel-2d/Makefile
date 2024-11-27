include ../../config.mk

EXTRA_FLAGS=

all: seidel-2d seidel-2d.wasm

seidel-2d: seidel-2d.c seidel-2d.h
	$(VERBOSE) $(CC) -o seidel-2d seidel-2d.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

seidel-2d.wasm: seidel-2d.c seidel-2d.h
	$(VERBOSE) $(CC_WASM) -o seidel-2d.wasm seidel-2d.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f seidel-2d seidel-2d.wasm
