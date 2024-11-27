include ../../config.mk

EXTRA_FLAGS=-lm

all: correlation correlation.wasm

correlation: correlation.c correlation.h
	$(VERBOSE) $(CC) -o correlation correlation.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

correlation.wasm: correlation.c correlation.h
	$(VERBOSE) $(CC_WASM) -o correlation.wasm correlation.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f correlation correlation.wasm
