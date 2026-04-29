from Calculator.history import history
import logging

def get_command():
    return input("Enter command: ")

def get_operand():
    return float(input("Enter an operand: "))

def unknown_command(command):
    logging.warning(f"Unknown command '{command}'")
    print("The calculator does not know this command.")

def command_clear():
    my_calc_history = history()
    return my_calc_history

def command_exit():
    print("Exiting calculator...")
