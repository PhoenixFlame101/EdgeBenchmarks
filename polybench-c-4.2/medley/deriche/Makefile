include ../../config.mk

EXTRA_FLAGS=

all: deriche deriche.wasm

deriche: deriche.c deriche.h
	$(VERBOSE) $(CC) -o deriche deriche.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

deriche.wasm: deriche.c deriche.h
	$(VERBOSE) $(CC_WASM) -o deriche.wasm deriche.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f deriche deriche.wasm
