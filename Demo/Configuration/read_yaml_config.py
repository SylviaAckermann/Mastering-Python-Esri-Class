import yaml

from pathlib import Path

config_file_path = Path("config.yaml")

with config_file_path.open(encoding="UTF8") as config_file:
    config = yaml.load(config_file, Loader=yaml.SafeLoader)

    print(config)