from Calculator.history import history

def get_command():
    return input("Enter command: ")

def get_operand():
    return float(input("Enter an operand: "))

def command_clear():
    my_calc_history = history()
    return my_calc_history

def command_exit():
    print("Exiting calculator...")
