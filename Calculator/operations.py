from Calculator.history import history
import logging, os, re
from Calculator.files import is_filename

def get_command():
    user_input = input("Enter command: ")
    #CALC_RE = re.compile(r"^(add|subtract|multiply|divide)\s+(-?\d+(?:\.\d+)?)$")
    r = re.compile(r"(?P<op_name>\w+) (?P<op_value>\d+)")
    match = r.search(user_input)  # Use search instead of finditer
    if match:
        d = match.groupdict()
        d['op_value'] = float(d['op_value'])
        return d['op_name'], d['op_value']
    else:
        # No match found, return just the command
        # for command = history, clear, exit, save, load
        return user_input, 0

def get_operand():
    return float(input("Enter an operand: "))

def get_history_json():
    my_calc_history = history()
    print("Would you like to reuse the history of your previous calculations?")
    history_file = input("If yes, enter path to history.json here: ")
    if is_filename(history_file):
        if os.path.exists(history_file):
            try:
                my_calc_history.load_history(history_file)
                print(f"Loaded history from {history_file}.")
            except Exception:
                logging.error("History could not be loaded.")
        else:
            print("Continuing without loading history.")
        return my_calc_history

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
 