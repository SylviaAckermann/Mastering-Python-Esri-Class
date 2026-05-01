from Calculator.operations import get_operand, write_command
from Calculator.history_entry import HistoryEntry

def add(result, operand):
    result = result + operand
    symbol = "+"
    return result, symbol, operand

def sub(result, operand):
    result =  result - operand
    symbol = "-"
    return result, symbol, operand

def mul(result, operand):
    result =  result * operand
    symbol = "*"
    return result, symbol, operand

def div(result, operand):
    try:
        result = result / operand
    except ZeroDivisionError:
        print("Division by zero would lead to infinity. Please choose another operand.")
        operand = get_operand()
        result, _, _ = div(result,operand)
    symbol = "/"
    return result, symbol, operand


def get_command_function(command):
    if command == "add" or command == "+":
        return add
    elif command == "subtract" or command == "-":
        return sub
    elif command == "multiply" or command == "*":
        return mul
    elif command == "divide" or command == "/":
        return div
    

def command_calc(calc_fn, command_name, operand, history):
    value = calculate_result(history)
    value, symbol, operand = calc_fn(value, operand)
    print_result(value)
    id = history.increase_history_id()
    new_history_entry = HistoryEntry(id, command_name, symbol, operand)
    history.append_entry(new_history_entry)
    write_command(command_name, operand)
    return history


def calculate_result(history):
    value = 0
    for entry in history:
        calc_fn = get_command_function(entry.op_name)
        value, _ ,_ = calc_fn(value, entry.op_value)
    return value


def print_result(result):
    print("Result: "+str(result))
