include ../../../config.mk

EXTRA_FLAGS=-lm

all: gramschmidt gramschmidt.wasm

gramschmidt: gramschmidt.c gramschmidt.h
	$(VERBOSE) $(CC) -o gramschmidt gramschmidt.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

gramschmidt.wasm: gramschmidt.c gramschmidt.h
	$(VERBOSE) $(CC_WASM) -o gramschmidt.wasm gramschmidt.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f gramschmidt gramschmidt.wasm
