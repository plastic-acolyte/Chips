class BankError(Exception):
    def __init__(self):
        super().__init__("Not enough chips in the bank")


class HandError(Exception):
    def __init__(self, command: str, is_empty: bool):
        if is_empty:
            super().__init__("Tried to {} with an empty hand".format(command))
        else:
            super().__init__("Tried to {} with a full hand".format(command))
