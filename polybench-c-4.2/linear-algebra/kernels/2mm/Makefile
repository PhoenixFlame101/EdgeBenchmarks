include ../../../config.mk

EXTRA_FLAGS=

all: 2mm 2mm.wasm

2mm: 2mm.c 2mm.h
	$(VERBOSE) $(CC) -o 2mm 2mm.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

2mm.wasm: 2mm.c 2mm.h
	$(VERBOSE) $(CC_WASM) -o 2mm.wasm 2mm.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f 2mm 2mm.wasm
