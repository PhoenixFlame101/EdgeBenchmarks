include ../../config.mk

EXTRA_FLAGS=

all: covariance covariance.wasm

covariance: covariance.c covariance.h
	$(VERBOSE) $(CC) -o covariance covariance.c $(CFLAGS) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

covariance.wasm: covariance.c covariance.h
	$(VERBOSE) $(CC_WASM) -o covariance.wasm covariance.c $(CFLAGS_WASM) -I. -I../../utilities ../../utilities/polybench.c $(EXTRA_FLAGS)

clean:
	@ rm -f covariance covariance.wasm
