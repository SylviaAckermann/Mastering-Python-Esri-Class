import Calculator.commands 

def get_command_function(command):
    if command == "add" or command == "+":
        return add
    elif command == "subtract" or command == "-":
        return sub
    elif command == "multiply" or command == "*":
        return mul
    elif command == "divide" or command == "/":
        return div

def calculate_result(calc_history):
    value = 0
    for calc in calc_history:
        calc_fn = get_command_function(calc["command"])
        value = calc_fn(value, calc["operand"])
    print_result(value)
    return value

def print_result(result):
    print("Result: "+str(result))