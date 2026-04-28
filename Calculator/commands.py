

from Calculator.history import print_history_commands, print_history_calculations, remove_id_from_history
from Calculator.operations import get_command, get_operand, command_clear, command_exit, print_result

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


def command_calc(calc_fn, command_name, operand):
    global value, history_id
    #operand = float(input("Please enter an operand: "))
    value, symbol = calc_fn(value, operand)
    print_result(value)
    history_id += 1
    calc_history.append({"id": history_id,"command": command_name, "symbol": symbol, "operand": operand})


def command_loop():
    global value, calc_history, history_id
    history_id = 0

    while True: 
        command = get_command()

        if command == "clear":
            value, calc_history = command_clear()
            print_result(value)
        elif command == "exit":
            command_exit()
            break
        elif command == "remove":
            calc_history = remove_id_from_history(calc_history)
            print_history_commands(calc_history)
            continue
        elif command == "history":
            print_history_calculations(calc_history)
            print_result(value)

        else:
            operand = get_operand()

            if command == "add" or command == "+":
                command_calc(add, command, operand)
            elif command == "subtract" or command == "-":
                command_calc(sub, command, operand)
            elif command == "multiply" or command == "*":
                command_calc(mul, command, operand)
            elif command == "divide" or command == "/":
                command_calc(div, command, operand)
            else:
                print("The calculator does not know this command.")
