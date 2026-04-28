

from Calculator.history import print_history_commands, print_history_calculations, remove_id_from_history
from Calculator.operations import get_command, get_operand, command_clear, command_exit
#from Calculator.result import print_result, calculate_result

value = 0
calc_history = []

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
    symbol = "-"
    return result, symbol

def div(result, operand):
    result =  result / operand
    symbol = "/"
    return result, symbol


def command_calc(calc_fn, command_name):
    global value, history_id, calc_history
    operand = get_operand()
    value = calculate_result(calc_history)
    value, symbol = calc_fn(value, operand)
    print_result(value)
    history_id += 1
    calc_history.append({"id": history_id,"command": command_name, "symbol": symbol, "operand": operand})

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
        value, _ = calc_fn(value, calc["operand"])
    return value

def print_result(result):
    print("Result: "+str(result))

def command_loop():
    global value, calc_history, history_id
    history_id = 0

    while True: 
        command = get_command()

        if command == "clear":
            value, calc_history = command_clear()
            calculate_result(calc_history)
        elif command == "exit":
            command_exit()
            break
        elif command == "remove":
            calc_history = remove_id_from_history(calc_history)
            print_history_commands(calc_history)
            continue
        elif command == "history":
            print_history_commands(calc_history)
            print_history_calculations(calc_history)
            result = calculate_result(calc_history)
            print_result(result)

        else:
            
            if command == "add" or command == "+":
                command_calc(add, command)
            elif command == "subtract" or command == "-":
                command_calc(sub, command)
            elif command == "multiply" or command == "*":
                command_calc(mul, command)
            elif command == "divide" or command == "/":
                command_calc(div, command)
            else:
                print("The calculator does not know this command.")
