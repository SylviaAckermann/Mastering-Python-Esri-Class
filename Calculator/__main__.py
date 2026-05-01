from Calculator.commands import command_loop
import logging
from Calculator.files import read_config

# Import logging here to only load function once
config = read_config("Calculator/config.yaml")
logging.basicConfig(
    filename=config["log_file"],
    format="%(levelname)s: %(message)s",
    level=config["log_level"],
)


def main():

    print("Calculator Tool")
    print(
        "Available commands: add, subtract, multiply, divide, clear, history, remove, exit"
    )

    command_loop()


if __name__ == "__main__":
    main()
