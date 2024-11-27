include ../../../config.mk

EXTRA_FLAGS=

all: 3mm 3mm.wasm

3mm: 3mm.c 3mm.h
	$(VERBOSE) $(CC) -o 3mm 3mm.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

3mm.wasm: 3mm.c 3mm.h
	$(VERBOSE) $(CC_WASM) -o 3mm.wasm 3mm.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f 3mm 3mm.wasm
