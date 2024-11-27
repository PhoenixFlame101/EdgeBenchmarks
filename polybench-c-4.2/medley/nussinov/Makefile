include ../../config.mk

EXTRA_FLAGS=

all: nussinov nussinov.wasm

nussinov: nussinov.c nussinov.h
	$(VERBOSE) $(CC) -o nussinov nussinov.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

nussinov.wasm: nussinov.c nussinov.h
	$(VERBOSE) $(CC_WASM) -o nussinov.wasm nussinov.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f nussinov nussinov.wasm
