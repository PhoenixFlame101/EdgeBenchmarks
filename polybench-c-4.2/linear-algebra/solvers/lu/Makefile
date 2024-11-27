include ../../../config.mk

EXTRA_FLAGS=

all: lu lu.wasm

lu: lu.c lu.h
	$(VERBOSE) $(CC) -o lu lu.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

lu.wasm: lu.c lu.h
	$(VERBOSE) $(CC_WASM) -o lu.wasm lu.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f lu lu.wasm
