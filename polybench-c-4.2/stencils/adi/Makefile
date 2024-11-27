include ../../config.mk

EXTRA_FLAGS=

all: adi adi.wasm

adi: adi.c adi.h
	$(VERBOSE) $(CC) -o adi adi.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

adi.wasm: adi.c adi.h
	$(VERBOSE) $(CC_WASM) -o adi.wasm adi.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f adi adi.wasm
