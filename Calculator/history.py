import json, csv
from Calculator.history_entry import HistoryEntry
from Calculator.files import is_filename

class historyIterator:
    def __init__(self, items):
        self.__items = items
        self.__index = 0

    def __next__(self):
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            self.__index += 1
            return item
        raise StopIteration

class history:

    def __init__(self):
        self.__history_id = 0
        self.__calc_history = []

    def __iter__(self):
        return iter(self.__calc_history)

    def append_entry(self, entry):
        self.__calc_history.append(entry)

    def get_calc_history(self):
        return self.__calc_history
    
    def increase_history_id(self):
        self.__history_id += 1
        return self.__history_id
    
    def print_history_commands(self):
        for entry in self:
            print(entry.to_dict())

    def print_history_calculations(self):
        print("0")
        for c in self:
            print(c.symbol+" "+str(c.op_value)+" ") 

    def remove_id_from_history(self, history_id_remove):
        for idx, calculation in enumerate(self):
            if calculation.id == int(history_id_remove):
                del self.__calc_history[idx]
                break  # Exit after removing the first match
        return self


    def load_history_json(self, json_file_name):
        try:
            with open(json_file_name, "r", encoding="utf-8") as history_file:
                loaded_data = json.load(history_file)
                # Convert dicts back to HistoryEntry objects
                self.__calc_history = [
                    HistoryEntry(entry["id"], entry["command"], entry["symbol"], entry["operand"])
                    for entry in loaded_data
                ]
                # Update history_id to the highest existing ID
                if self.__calc_history:
                    self.__history_id = max(entry.id for entry in self.__calc_history)
        except FileNotFoundError:
            print(f"History file {json_file_name} not found. Starting with empty history.")
        except json.JSONDecodeError:
            print(f"Error reading history file {json_file_name}. Starting with empty history.")
    

    def save_history_json(self, json_file_name):
        if is_filename(json_file_name):
            with open(json_file_name, "w", encoding="utf-8") as history_file:
                entries_as_dicts = [entry.to_dict() for entry in self]
                json.dump(entries_as_dicts, history_file, indent=2)


    def save_history_csv(self, csv_file_name):
        if is_filename(csv_file_name):
            with open(csv_file_name, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "command", "symbol", "operand"])
                writer.writeheader()
                entries_as_dicts = [entry.to_dict() for entry in self]
                writer.writerows(entries_as_dicts)




