from Calculator.history import history
import logging, os, re
from Calculator.files import is_filename

def get_command():
    return input("Enter command: ")

def get_operand():
    return float(input("Enter an operand: "))

# def get_history_json():
#     my_calc_history = history()
#     print("Would you like to reuse the history of your previous calculations?")
#     history_file = input("If yes, enter path to history.json here: ")
#     if is_filename(history_file):
#         if os.path.exists(history_file):
#             try:
#                 my_calc_history.load_history(history_file)
#                 print(f"Loaded history from {history_file}.")
#             except Exception:
#                 logging.error("History could not be loaded.")
#         else:
#             print("Continuing without loading history.")
#         return my_calc_history

def write_command(command, operand):
    logging.info(f"command '{command} {operand}'")

def unknown_command(command):
    logging.warning(f"Unknown command '{command}'")
    print("The calculator does not know this command.")

def command_clear():
    my_calc_history = history()
    return my_calc_history

def command_exit():
    print("Exiting calculator...")
 