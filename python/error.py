class BankError(Exception):
    def __init__(self):
        super().__init__("Not enough chips in the bank")


class HandError(Exception):
    def __init__(self, command: str, has_chip: bool):
        if has_chip:
            super().__init__("Tried to {} while already holding a chip".format(command))
        else:
            super().__init__("Tried to {} while not holding a chip".format(command))
