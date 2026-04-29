
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
        history.print_history_commands(self)
        history_id_remove = input("Which ID of the history should be removed? ")
        for idx, calculation in enumerate(self.calc_history):
            if calculation["id"] == int(history_id_remove):
                del self.calc_history[idx]
        return self



