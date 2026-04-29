
from Calculator.operations import get_command, get_history_json, unknown_command, command_clear, command_exit
from Calculator.calc_result import command_calc, calculate_result, print_result, add, sub, mul, div
from Calculator.history import history


def command_loop():

    my_calc_history = get_history_json()

    while True: 
        command = get_command()

        if command == "clear":
            my_calc_history = command_clear()
            result = calculate_result(my_calc_history.calc_history)
            print_result(result)
        elif command == "exit":
            command_exit()
            break
        elif command == "remove":
            my_calc_history = history.remove_id_from_history(my_calc_history)
            history.print_history_commands(my_calc_history)
            continue
        elif command == "history":
            history.print_history_commands(my_calc_history)
            history.print_history_calculations(my_calc_history)
            result = calculate_result(my_calc_history.calc_history)
            print_result(result)

        else:
            
            if command == "add" or command == "+":
                my_calc_history = command_calc(add, command, my_calc_history)
            elif command == "subtract" or command == "-":
                my_calc_history = command_calc(sub, command, my_calc_history)
            elif command == "multiply" or command == "*":
                my_calc_history = command_calc(mul, command, my_calc_history)
            elif command == "divide" or command == "/":
                my_calc_history = command_calc(div, command, my_calc_history)
            else:
                unknown_command(command)
