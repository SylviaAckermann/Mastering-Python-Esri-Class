import json


class history:

    def __init__(self):
        self.history_id = 0
        self.calc_history = []


    def print_history_commands(self):
        for calculation in self.calc_history:
            print(calculation)

    def print_history_calculations(self):
        print("0")
        for c in self.calc_history:
            print(c["symbol"]+" "+str(c["operand"])+" ") 

    def remove_id_from_history(self):
        self.print_history_commands()
        history_id_remove = input("Which ID of the history should be removed? ")
        for idx, calculation in enumerate(self.calc_history):
            if calculation["id"] == int(history_id_remove):
                del self.calc_history[idx]
                break  # Exit after removing the first match
        return self
    
    def save_history(self, json_file_name):
        with open(json_file_name, "w", encoding="utf-8") as history_file:
            json.dump(self.calc_history, history_file, indent=2)

    def load_history(self, json_file_name):
        try:
            with open(json_file_name, "r", encoding="utf-8") as history_file:
                self.calc_history = json.load(history_file)
                # Update history_id to the highest existing ID
                if self.calc_history:
                    self.history_id = max(entry["id"] for entry in self.calc_history)
        except FileNotFoundError:
            print(f"History file {json_file_name} not found. Starting with empty history.")
        except json.JSONDecodeError:
            print(f"Error reading history file {json_file_name}. Starting with empty history.")




