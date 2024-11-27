include ../../../config.mk

EXTRA_FLAGS=

all: ludcmp ludcmp.wasm

ludcmp: ludcmp.c ludcmp.h
	$(VERBOSE) $(CC) -o ludcmp ludcmp.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

ludcmp.wasm: ludcmp.c ludcmp.h
	$(VERBOSE) $(CC_WASM) -o ludcmp.wasm ludcmp.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f ludcmp ludcmp.wasm
