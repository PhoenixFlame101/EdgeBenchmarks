include ../../../config.mk

EXTRA_FLAGS=

all: syr2k syr2k.wasm

syr2k: syr2k.c syr2k.h
	$(VERBOSE) $(CC) -o syr2k syr2k.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

syr2k.wasm: syr2k.c syr2k.h
	$(VERBOSE) $(CC_WASM) -o syr2k.wasm syr2k.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f syr2k syr2k.wasm
