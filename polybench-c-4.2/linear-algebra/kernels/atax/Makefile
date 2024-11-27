include ../../../config.mk

EXTRA_FLAGS=

all: atax atax.wasm

atax: atax.c atax.h
	$(VERBOSE) $(CC) -o atax atax.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

atax.wasm: atax.c atax.h
	$(VERBOSE) $(CC_WASM) -o atax.wasm atax.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f atax atax.wasm
