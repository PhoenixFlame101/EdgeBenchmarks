include ../../config.mk

EXTRA_FLAGS=

all: heat-3d heat-3d.wasm

heat-3d: heat-3d.c heat-3d.h
	$(VERBOSE) $(CC) -o heat-3d heat-3d.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

heat-3d.wasm: heat-3d.c heat-3d.h
	$(VERBOSE) $(CC_WASM) -o heat-3d.wasm heat-3d.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f heat-3d heat-3d.wasm
