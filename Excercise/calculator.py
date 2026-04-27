
value = 0
calc_history = []

while True: 
    command = input("Enter command: ")

    if command == "clear":
        value = 0
    elif command == "exit":
        break
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
            calc_history.append({"id": len(calc_history),"command": command, "symbol": symbol, "operand": operand})
    print("Result: "+str(value))
