include ../../../config.mk

EXTRA_FLAGS=

all: symm symm.wasm

symm: symm.c symm.h
	$(VERBOSE) $(CC) -o symm symm.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

symm.wasm: symm.c symm.h
	$(VERBOSE) $(CC_WASM) -o symm.wasm symm.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f symm symm.wasm
