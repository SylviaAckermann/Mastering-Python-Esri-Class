
import __main__

def print_history_commands():
    for calculation in __main__.calc_history:
        print(calculation)

def print_history_calculations():
    print("0")
    for c in __main__.calc_history:
        print(c["symbol"]+" "+str(c["operand"])+" ")

def remove_id_from_history():
    global calc_history
    print_history_commands()
    history_id_remove = input("Which ID of the history should be removed? ")
    for idx, calculation in enumerate(__main__.calc_history):
        if calculation["id"] == int(history_id_remove):
            del __main__.calc_history[idx]
    return __main__.calc_history