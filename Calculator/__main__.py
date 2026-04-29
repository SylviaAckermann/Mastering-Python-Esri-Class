
from Calculator.commands import command_loop
import logging

# Import logging here to only load function once
logging.basicConfig(
    filename="Calculator/calc_commands.log",
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)

def main():

    print("Calculator Tool")
    print("Available commands: add, subtract, multiply, divide, clear, history, remove, exit")

    command_loop()

if __name__ =="__main__":
    main()