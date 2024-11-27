include ../../../config.mk

EXTRA_FLAGS=

all: mvt mvt.wasm

mvt: mvt.c mvt.h
	$(VERBOSE) $(CC) -o mvt mvt.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

mvt.wasm: mvt.c mvt.h
	$(VERBOSE) $(CC_WASM) -o mvt.wasm mvt.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f mvt mvt.wasm
