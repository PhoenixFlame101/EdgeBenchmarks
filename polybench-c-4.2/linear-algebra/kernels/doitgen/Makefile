include ../../../config.mk

EXTRA_FLAGS=

all: doitgen doitgen.wasm

doitgen: doitgen.c doitgen.h
	$(VERBOSE) $(CC) -o doitgen doitgen.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

doitgen.wasm: doitgen.c doitgen.h
	$(VERBOSE) $(CC_WASM) -o doitgen.wasm doitgen.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f doitgen doitgen.wasm
