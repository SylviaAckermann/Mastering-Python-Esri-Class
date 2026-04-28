
def print_history():
    print("0")
    for c in calc_history:
        print(c["symbol"]+" "+str(c["operand"])+" ")

def clear_calculator():
    global value, calc_history 
    value = 0
    calc_history = []

def remove_id_from_history():
    global calc_history
    print(calc_history)
    history_id_remove = input("Which ID of the history should be removed?")
    for idx, calculation in enumerate(calc_history):
        if calculation["id"] == int(history_id_remove):
            del calc_history[idx]
    return calc_history

history_id = 0
clear_calculator()

while True: 
    command = input("Enter command: ")

    if command == "clear":
        clear_calculator()
    elif command == "exit":
        break
    elif command == "remove":
        remove_id_from_history()
        print_history()
    elif command == "history":
        print_history()

    else:
        operand = float(input("Enter an operand: "))

        if command == "add":
            value = value + operand
            symbol = "+"
        elif command == "subtract":
            value = value - operand
            symbol = "-"
        elif command == "multiply":
            value = value * operand
            symbol = "*"
        elif command == "divide":
            value = value / operand
            symbol = "/"
        else:
            print("The calculator does not know this command.")
            symbol = " "

        if symbol != " ":
            history_id += 1
            calc_history.append({"id": history_id,"command": command, "symbol": symbol, "operand": operand})
    print("Result: "+str(value))
