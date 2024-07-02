from enum import Enum, auto
from queue import SimpleQueue


class TokenType(Enum):
    COMMAND = auto()
    REGISTER = auto()
    INT = auto()


class Command(Enum):
    ADD = "ADD"
    BANK = "BANK"
    DRAW = "DRAW"
    EAT = "EAT"
    END = "END"
    FLIP = "FLIP"
    GAMBIT = "GAMBIT"
    NEXT = "NEXT"
    POP = "POP"
    PREV = "PREV"
    PUSH = "PUSH"
    SUB = "SUB"
    SWAP = "SWAP"
    WAGER = "WAGER"
    WHILE = "WHILE"


class Register(Enum):
    HAND = "HAND"
    TOP = "TOP"


class Token:
    type: TokenType
    value: Command | Register | int

    def __init__(self, value: str):
        if value.isnumeric() or value[0] == '-' and value[1:].isnumeric():
            self.type = TokenType.INT
            self.value = int(value)

        elif value in Register:
            self.type = TokenType.REGISTER
            self.value = Register[value]

        elif value in Command:
            self.type = TokenType.COMMAND
            self.value = Command[value]

        else:
            raise ValueError


class Tokenizer:
    tokens: SimpleQueue[Token]

    def __init__(self, filepath):
        self.tokens = SimpleQueue()

        with open(filepath) as file:
            for line in file:
                line = line.split('#', maxsplit=1)[0].strip().upper()

                for value in line.split():
                    self.tokens.put(Token(value))

    def has_next(self) -> bool:
        return self.tokens.empty()

    def next(self) -> Token:
        return self.tokens.get()
