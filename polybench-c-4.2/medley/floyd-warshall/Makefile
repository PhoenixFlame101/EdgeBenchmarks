include ../../config.mk

EXTRA_FLAGS=

all: floyd-warshall floyd-warshall.wasm

floyd-warshall: floyd-warshall.c floyd-warshall.h
	$(VERBOSE) $(CC) -o floyd-warshall floyd-warshall.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

floyd-warshall.wasm: floyd-warshall.c floyd-warshall.h
	$(VERBOSE) $(CC_WASM) -o floyd-warshall.wasm floyd-warshall.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f floyd-warshall floyd-warshall.wasm
