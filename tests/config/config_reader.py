import yaml
import os

def get_config():
    # base_dir =
    with open("tests/config/config.yml") as f:
        return yaml.safe_load(f)