OUT_DIR ?= $(abspath .)

PY ?= python3

.PHONY: default all clean format

PY_FILES := $(wildcard *.py)

%.py:
	black $@

format: $(PY_FILES)

harness:
	-rm -rf $(OUT_DIR)/libharness.so
	$(PY) harness.py $(OUT_DIR) libharness.so

default: harness


all: default

clean:
	-rm -rf libharness.so

$(shell mkdir -p $(DIRS))
