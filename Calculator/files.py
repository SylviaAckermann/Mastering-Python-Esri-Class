import re

def is_filename(file):
    r = re.compile(r"\s")  # Regex to match any whitespace character
    if r.search(file):
        print(f"Warning: Filename '{file}' is invalid and contains whitespaces.")
        return False
    return True