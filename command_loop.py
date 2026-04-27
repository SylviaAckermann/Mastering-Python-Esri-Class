
while True:
    command = input("Enter a command: ")

    if command == "exit":
        break
    elif command == "version":
        print("0.0.1")
        continue
    else:
        print(command)
