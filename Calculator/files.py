import re, yaml
from pathlib import Path


def is_filename(file):
    r = re.compile(r"\s")  # Regex to match any whitespace character
    if r.search(file):
        print(f"Warning: Filename '{file}' is invalid and contains whitespaces.")
        return False
    return True


def get_file_type(file):
    ext = Path(file).suffix
    if not ext:
        return None
    return ext.lower().lstrip(".")


def read_config(config_file):
    config_file_path = Path(config_file)

    with config_file_path.open(encoding="UTF8") as config_file:
        config = yaml.load(config_file, Loader=yaml.SafeLoader)

        print(config)
    return config
