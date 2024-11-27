include ../../../config.mk

EXTRA_FLAGS=

all: trmm trmm.wasm

trmm: trmm.c trmm.h
	$(VERBOSE) $(CC) -o trmm trmm.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

trmm.wasm: trmm.c trmm.h
	$(VERBOSE) $(CC_WASM) -o trmm.wasm trmm.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f trmm trmm.wasm
