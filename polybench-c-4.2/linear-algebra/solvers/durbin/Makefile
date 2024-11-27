include ../../../config.mk

EXTRA_FLAGS=

all: durbin durbin.wasm

durbin: durbin.c durbin.h
	$(VERBOSE) $(CC) -o durbin durbin.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

durbin.wasm: durbin.c durbin.h
	$(VERBOSE) $(CC_WASM) -o durbin.wasm durbin.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f durbin durbin.wasm
