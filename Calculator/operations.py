
def get_command():
    return input("Enter command: ")

def get_operand():
    return float(input("Enter an operand: "))

def command_clear():
    global value, calc_history 
    value = 0
    calc_history = []

def command_exit():
    print("Exiting calculator...")

