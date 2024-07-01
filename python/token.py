from enum import Enum


class Token(Enum):
    ADD = "ADD"
    BANK = "BANK"
    DRAW = "DRAW"
    EAT = "EAT"
    FLIP = "FLIP"
    NEXT = "NEXT"
    POP = "POP"
    PREV = "PREV"
    PUSH = "PUSH"
    SUB = "SUB"
    SWAP = "SWAP"
    WAGER = "WAGER"

    @staticmethod
    def parse(value):
        match value:
            case "ADD": return Token.ADD
            case "BANK": return Token.BANK
            case "DRAW": return Token.DRAW
            case "EAT": return Token.EAT
            case "FLIP": return Token.FLIP
            case "NEXT": return Token.NEXT
            case "POP": return Token.POP
            case "PREV": return Token.PREV
            case "PUSH": return Token.PUSH
            case "SUB": return Token.SUB
            case "SWAP": return Token.SWAP
            case "WAGER": return Token.WAGER
