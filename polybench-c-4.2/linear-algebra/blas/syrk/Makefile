include ../../../config.mk

EXTRA_FLAGS=

all: syrk syrk.wasm

syrk: syrk.c syrk.h
	$(VERBOSE) $(CC) -o syrk syrk.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

syrk.wasm: syrk.c syrk.h
	$(VERBOSE) $(CC_WASM) -o syrk.wasm syrk.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f syrk syrk.wasm
