include ../../../config.mk

EXTRA_FLAGS=

all: gemm gemm.wasm

gemm: gemm.c gemm.h
	$(VERBOSE) $(CC) -o gemm gemm.c $(CFLAGS) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

gemm.wasm: gemm.c gemm.h
	$(VERBOSE) $(CC_WASM) -o gemm.wasm gemm.c $(CFLAGS_WASM) -I. -I../../../utilities ../../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f gemm gemm.wasm
