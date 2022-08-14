OUT_DIR ?= $(abspath .)

PY ?= python3
CC ?= gcc

.PHONY: all clean format

PY_FILES := $(wildcard *.py)

%.py:
	black $@

format: $(PY_FILES)

build: test.c
	gcc test.c -L. -l harness -o test

harness:
	-rm -rf $(OUT_DIR)/libharness.so
	$(PY) harness.py $(OUT_DIR) libharness.so

all: harness build

clean:
	-rm -rf libharness.so

$(shell mkdir -p $(DIRS))
