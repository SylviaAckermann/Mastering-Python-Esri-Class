
class HistoryEntry:
    def __init__(self, id, op_name, symbol, op_value):
        self.id = id
        self.op_name = op_name
        self.symbol = symbol
        self.op_value = op_value

    def to_dict(self):
        return {
            "id": self.id,
            "command": self.op_name,
            "symbol": self.symbol,
            "operand": self.op_value
        }


# Update the rest of the application to use the HistoryEntry class instead of 
# the dictionary which is being used to store each history entry