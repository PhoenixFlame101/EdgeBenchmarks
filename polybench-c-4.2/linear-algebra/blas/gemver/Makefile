include ../../../config.mk

EXTRA_FLAGS=

all: gemver gemver.wasm

gemver: gemver.c gemver.h
	$(VERBOSE) $(CC) -o gemver gemver.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

gemver.wasm: gemver.c gemver.h
	$(VERBOSE) $(CC_WASM) -o gemver.wasm gemver.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f gemver gemver.wasm
