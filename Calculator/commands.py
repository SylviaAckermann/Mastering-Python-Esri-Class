
import __main__
from Calculator.history import print_history_commands, print_history_calculations, remove_id_from_history
from Calculator.operations import get_command, get_operand, command_clear, command_exit

def command_loop():
    global value, calc_history
    history_id = 0

    while True: 
        command = get_command()

        if command == "clear":
            command_clear()
        elif command == "exit":
            command_exit()
            break
        elif command == "remove":
            remove_id_from_history()
            print_history_commands()
            continue
        elif command == "history":
            print_history_calculations()

        else:
            operand = get_operand()

            if command == "add":
                value = __main__.value + operand
                symbol = "+"
            elif command == "subtract":
                value = __main__.value - operand
                symbol = "-"
            elif command == "multiply":
                value = __main__.value * operand
                symbol = "*"
            elif command == "divide":
                value = __main__.value / operand
                symbol = "/"
            else:
                print("The calculator does not know this command.")
                symbol = " "
                continue

        history_id += 1
        __main__.calc_history.append({"id": history_id,"command": command, "symbol": symbol, "operand": operand})
        print("Result: "+str(value))