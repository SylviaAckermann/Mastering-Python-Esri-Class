

from Calculator.history import print_history_commands, print_history_calculations, remove_id_from_history
from Calculator.operations import get_command, get_operand, command_clear, command_exit
from Calculator.calc_result import command_calc, calculate_result, print_result, add, sub, mul, div

value = 0
calc_history = []

def command_calc(calc_fn, command_name, calc_history):
    global value, history_id
    operand = get_operand()
    value = calculate_result(calc_history)
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
                command_calc(add, command, calc_history)
            elif command == "subtract" or command == "-":
                command_calc(sub, command, calc_history)
            elif command == "multiply" or command == "*":
                command_calc(mul, command, calc_history)
            elif command == "divide" or command == "/":
                command_calc(div, command, calc_history)
            else:
                print("The calculator does not know this command.")
