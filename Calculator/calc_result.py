from Calculator.operations import get_operand

def add(result, operand):
    result = result + operand
    symbol = "+"
    return result, symbol

def sub(result, operand):
    result =  result - operand
    symbol = "-"
    return result, symbol

def mul(result, operand):
    result =  result * operand
    symbol = "*"
    return result, symbol

def div(result, operand):
    result =  result / operand
    symbol = "/"
    return result, symbol


def get_command_function(command):
    if command == "add" or command == "+":
        return add
    elif command == "subtract" or command == "-":
        return sub
    elif command == "multiply" or command == "*":
        return mul
    elif command == "divide" or command == "/":
        return div
    

def command_calc(calc_fn, command_name, calc_history):
    global value, history_id
    operand = get_operand()
    value = calculate_result(calc_history)
    value, symbol = calc_fn(value, operand)
    print_result(value)
    history_id += 1
    calc_history.append({"id": history_id,"command": command_name, "symbol": symbol, "operand": operand})


def calculate_result(calc_history):
    value = 0
    for calc in calc_history:
        calc_fn = get_command_function(calc["command"])
        value, _ = calc_fn(value, calc["operand"])
    return value


def print_result(result):
    print("Result: "+str(result))