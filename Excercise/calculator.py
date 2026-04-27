
value = 0
history_id = 0
calc_history = []

while True: 
    command = input("Enter command: ")

    if command == "clear":
        value = 0
        calc_history = []
    elif command == "exit":
        break
    elif command == "remove":
        history_id_remove = input("Which ID of the history should be removed?")
        for i, c in enumerate(calc_history):
            if c["id"] == int(history_id_remove):
                del calc_history[i]
        print(calc_history)
    elif command == "history":
        print("0")
        for c in calc_history:
            print(c["symbol"]+" "+str(c["operand"])+" ")

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
