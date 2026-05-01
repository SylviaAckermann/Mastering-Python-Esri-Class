
from Calculator.operations import get_command, unknown_command, command_clear, command_exit
from Calculator.calc_result import command_calc, calculate_result, print_result, add, sub, mul, div
from Calculator.history import history
from Calculator.files import get_file_type
import re

CALC_PATTERN = re.compile(r"^(?P<name>add|subtract|multiply|divide)\s+(?P<operand>-?\d+(?:\.\d+)?)$")
REMOVE_PATTERN = re.compile(r"^(?P<name>remove)\s+(?P<operand>\d+)$")
FILE_PATTERN = re.compile(r"^(?P<name>save|load)\s+(?P<filename>\S+)$")
BARE_PATTERN = re.compile(r"^(?P<name>history|clear|exit)$")

def command_loop():

    my_calc_history = history()

    while True: 
        command = get_command()

        calc_match = CALC_PATTERN.match(command)
        remove_match = REMOVE_PATTERN.match(command)
        file_match = FILE_PATTERN.match(command)
        bare_match = BARE_PATTERN.match(command)

        if calc_match:
            command = calc_match["name"]
            number = float(calc_match["operand"])
            if command == "add" or command == "+":
                my_calc_history = command_calc(add, command, number, my_calc_history)
            elif command == "subtract" or command == "-":
                my_calc_history = command_calc(sub, command, number, my_calc_history)
            elif command == "multiply" or command == "*":
                my_calc_history = command_calc(mul, command, number, my_calc_history)
            elif command == "divide" or command == "/":
                my_calc_history = command_calc(div, command, number, my_calc_history)

        elif remove_match:
            my_calc_history = history.remove_id_from_history(my_calc_history, remove_match["operand"])
            history.print_history_commands(my_calc_history)

        elif file_match:
            filetype = get_file_type(file_match["filename"])
            if file_match["name"] == "load":
                print("Load history")
                if filetype == "json":
                    my_calc_history = history.load_history_json(file_match["filename"])
                elif filetype == "csv":
                    print("Loading history from csv is not implemented yet.")
            elif file_match["name"] == "save":
                if filetype == "json":
                    history.save_history_json(file_match["filename"])
                elif filetype == "csv":
                    history.save_history_csv(file_match["filename"])
                print(f"History saved to file {file_match["filename"]}")
        
        elif bare_match:
            if command == "exit":
                command_exit()
                break

            if command == "clear":
                my_calc_history = command_clear()
                result = calculate_result(my_calc_history.get_calc_history())
                print_result(result)              

            elif command == "history":
                history.print_history_commands(my_calc_history)
                history.print_history_calculations(my_calc_history)
                result = calculate_result(my_calc_history.get_calc_history())
                print_result(result)

        else:
            unknown_command(command)
