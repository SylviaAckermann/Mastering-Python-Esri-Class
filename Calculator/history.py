

def print_history_commands(calc_history):
    for calculation in calc_history:
        print(calculation)

def print_history_calculations(calc_history):
    print("0")
    for c in calc_history:
        print(c["symbol"]+" "+str(c["operand"])+" ") 

def remove_id_from_history(calc_history):
    print_history_commands(calc_history)
    history_id_remove = input("Which ID of the history should be removed? ")
    for idx, calculation in enumerate(calc_history):
        if calculation["id"] == int(history_id_remove):
            del calc_history[idx]
    return calc_history




