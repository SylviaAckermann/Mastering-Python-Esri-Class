import json, csv

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

    def append_entry(self, command, symbol, operand):
        self.__calc_history.append({"id": self.__history_id,"command": command, "symbol": symbol, "operand": operand})

    def get_calc_history(self):
        return self.__calc_history
    
    def increase_history_id(self):
        self.__history_id += 1
    
    def print_history_commands(self):
        for calculation in self:
            print(calculation)

    def print_history_calculations(self):
        print("0")
        for c in self:
            print(c["symbol"]+" "+str(c["operand"])+" ") 

    def remove_id_from_history(self):
        self.print_history_commands()
        history_id_remove = input("Which ID of the history should be removed? ")
        for idx, calculation in enumerate(self):
            if calculation["id"] == int(history_id_remove):
                del self.__calc_history[idx]
                break  # Exit after removing the first match
        return self
    
    def save_history(self, json_file_name):
        with open(json_file_name, "w", encoding="utf-8") as history_file:
            json.dump(self.__calc_history, history_file, indent=2)

    def load_history(self, json_file_name):
        try:
            with open(json_file_name, "r", encoding="utf-8") as history_file:
                self.__calc_history = json.load(history_file)
                # Update history_id to the highest existing ID
                if self.__calc_history:
                    self.__history_id = max(entry["id"] for entry in self)
        except FileNotFoundError:
            print(f"History file {json_file_name} not found. Starting with empty history.")
        except json.JSONDecodeError:
            print(f"Error reading history file {json_file_name}. Starting with empty history.")
    
    def save_history_csv(self, csv_file_name):
        with open(csv_file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "command", "symbol", "operand"])
            writer.writeheader()
            writer.writerows(self.__calc_history)




