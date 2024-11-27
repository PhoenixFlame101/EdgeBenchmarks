include ../../../config.mk

EXTRA_FLAGS=-lm

all: cholesky cholesky.wasm

cholesky: cholesky.c cholesky.h
	$(VERBOSE) $(CC) -o cholesky cholesky.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

cholesky.wasm: cholesky.c cholesky.h
	$(VERBOSE) $(CC_WASM) -o cholesky.wasm cholesky.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f cholesky cholesky.wasm
