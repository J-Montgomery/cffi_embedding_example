#!/usr/bin/env python3

import argparse
import cffi
import json
from pathlib import Path

API_HEADER = """
const char *decode(const char *msg);

"""
class Config:
    def __init__(self, config_path):
        with open(config_path) as configfile:
            self.config = json.load(configfile)

    def get_models_dir(self):
        if "models_dir" in self.config:
            return self.config["models_dir"]
        else:
            return "models/"

    def get_lib_name(self):
        if "lib_name" in self.config:
            return self.config["lib_name"]
        else:
            return "model"

    def get_model_utilities(self):
        if "model_utilities" in self.config:
            return self.config["model_utilities"]
        else:
            return []

    def get_bundled_utilities(self):
        if "bundled_utilities" in self.config:
            return self.config["bundled_utilities"]
        else:
            return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir")
    parser.add_argument("model_name")
    parser.add_argument("-c", "--config", help="JSON file containing build config", default="build_config.json")
    args = parser.parse_args()

    config = Config(args.config)
    ffibuilder = cffi.FFI()

    ffibuilder.embedding_api(API_HEADER)

    source = []
    model_list = [Path(x) for x in config.get_model_utilities()]
    model_list.extend(
        [x for x in Path(config.get_models_dir()).rglob("*.py") if x not in model_list]
    )

    for file in model_list:
        with open(file) as f:
            code = f.read()
            source.append(code + "\n")

    ffibuilder.embedding_init_code(source)

    target_name = config.get_lib_name() + ".*"
    ffibuilder.compile(target=target_name, verbose=True)

if __name__ == "__main__":
    main()