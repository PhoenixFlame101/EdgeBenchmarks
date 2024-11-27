include ../../../config.mk

EXTRA_FLAGS=

all: trisolv trisolv.wasm

trisolv: trisolv.c trisolv.h
	$(VERBOSE) $(CC) -o trisolv trisolv.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

trisolv.wasm: trisolv.c trisolv.h
	$(VERBOSE) $(CC_WASM) -o trisolv.wasm trisolv.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f trisolv trisolv.wasm
