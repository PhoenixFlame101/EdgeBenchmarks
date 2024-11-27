include ../../../config.mk

EXTRA_FLAGS=

all: gesummv gesummv.wasm

gesummv: gesummv.c gesummv.h
	$(VERBOSE) $(CC) -o gesummv gesummv.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

gesummv.wasm: gesummv.c gesummv.h
	$(VERBOSE) $(CC_WASM) -o gesummv.wasm gesummv.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f gesummv gesummv.wasm
