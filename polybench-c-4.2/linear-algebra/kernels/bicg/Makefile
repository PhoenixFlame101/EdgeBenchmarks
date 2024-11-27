include ../../../config.mk

EXTRA_FLAGS=

all: bicg bicg.wasm

bicg: bicg.c bicg.h
	$(VERBOSE) $(CC) -o bicg bicg.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

bicg.wasm: bicg.c bicg.h
	$(VERBOSE) $(CC_WASM) -o bicg.wasm bicg.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f bicg bicg.wasm
