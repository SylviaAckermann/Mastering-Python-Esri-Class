from Calculator.operations import get_operand

def add(result, operand):
    result = result + operand
    symbol = "+"
    return result, symbol, operand

def sub(result, operand):
    result =  result - operand
    symbol = "-"
    return result, symbol, operand

def mul(result, operand):
    result =  result * operand
    symbol = "*"
    return result, symbol, operand

def div(result, operand):
    try:
        result = result / operand
    except ZeroDivisionError:
        print("Division by zero would lead to infinity. Please choose another operand.")
        operand = get_operand()
        result, _, _ = div(result,operand)
    symbol = "/"
    return result, symbol, operand


def get_command_function(command):
    if command == "add" or command == "+":
        return add
    elif command == "subtract" or command == "-":
        return sub
    elif command == "multiply" or command == "*":
        return mul
    elif command == "divide" or command == "/":
        return div
    

def command_calc(calc_fn, command_name, history):
    operand = get_operand()
    value = calculate_result(history.calc_history)
    value, symbol, operand = calc_fn(value, operand)
    print_result(value)
    history.history_id += 1
    history.calc_history.append({"id": history.history_id,"command": command_name, "symbol": symbol, "operand": operand})
    return history


def calculate_result(calc_history):
    value = 0
    for calc in calc_history:
        calc_fn = get_command_function(calc["command"])
        value, _ ,_ = calc_fn(value, calc["operand"])
    return value


def print_result(result):
    print("Result: "+str(result))
