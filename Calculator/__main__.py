from Calculator.operations import command_clear
from Calculator.commands import command_loop

# Module-level variables
value = 0
calc_history = []

def main():
    print("This is my calculator")

    global value, calc_history
    command_clear()

    command_loop()

if __name__ =="__main__":
    main()