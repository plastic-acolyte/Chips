from enum import Enum
from queue import SimpleQueue


class Token(Enum):
    ADD = "ADD"
    BANK = "BANK"
    DRAW = "DRAW"
    EAT = "EAT"
    END = "END"
    FLIP = "FLIP"
    GAMBIT = "GAMBIT"
    HAND = "HAND"
    NEXT = "NEXT"
    NUM = "NUM"
    POP = "POP"
    PREV = "PREV"
    PUSH = "PUSH"
    SUB = "SUB"
    SWAP = "SWAP"
    TOP = "TOP"
    WAGER = "WAGER"
    WHILE = "WHILE"

    @staticmethod
    def parse(value: str):
        match value:
            case "ADD": return Token.ADD
            case "BANK": return Token.BANK
            case "DRAW": return Token.DRAW
            case "EAT": return Token.EAT
            case "END": return Token.END
            case "FLIP": return Token.FLIP
            case "GAMBIT": return Token.GAMBIT
            case "HAND": return Token.HAND
            case "NEXT": return Token.NEXT
            case "POP": return Token.POP
            case "PREV": return Token.PREV
            case "PUSH": return Token.PUSH
            case "SUB": return Token.SUB
            case "SWAP": return Token.SWAP
            case "TOP": return Token.TOP
            case "WAGER": return Token.WAGER
            case "WHILE": return Token.WHILE

        if value.isnumeric():
            return Token.NUM


class Reader:
    tokens: SimpleQueue

    def __init__(self, filepath):
        self.tokens = SimpleQueue()
        self.token_pointer = 0

        with open(filepath) as file:
            for line in file:
                line = line.split('#', maxsplit=1)[0].strip()

                if line == '':
                    continue

                for token in line.split():
                    self.tokens.put(token)

    def has_token(self) -> bool:
        return not self.tokens.empty()

    def get_token(self) -> tuple:
        value = self.tokens.get()
        token = Token.parse(value)

        if token == Token.NUM:
            return token, int(value)

        return (token,)
