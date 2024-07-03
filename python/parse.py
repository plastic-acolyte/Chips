from enum import Enum, auto
from queue import SimpleQueue
from typing import Self


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

    def num_parameters(self) -> int:
        if not self.type == TokenType.COMMAND:
            raise Exception

        match self.value:
            case Command.DRAW:
                return 1

            case Command.WHILE:
                return 1

            case _:
                return 0

    def is_block_command(self) -> bool:
        if not self.type == TokenType.COMMAND:
            raise Exception

        return self.value == Command.WHILE


class CommandData:
    token: Token
    parameters: list[Token]
    children: list[Self]

    def __init__(self, token: Token):
        if not token.type == TokenType.COMMAND:
            raise Exception

        self.token = token
        self.parameters = []
        self.children = []


class Parser:
    tokens: SimpleQueue[Token]

    def __init__(self, filepath):
        self.tokens = SimpleQueue()

        with open(filepath) as file:
            for line in file:
                line = line.split('#', maxsplit=1)[0].strip().upper()

                for value in line.split():
                    self.tokens.put(Token(value))

    def has_next(self) -> bool:
        return not self.tokens.empty()

    def next(self) -> CommandData:
        if not self.has_next():
            raise Exception

        data = CommandData(self.tokens.get())

        for _ in range(data.token.num_parameters()):
            data.parameters.append(self.tokens.get())

        if data.token.is_block_command():
            while True:
                child = self.next()

                if child.token.value == Command.END:
                    break

                data.children.append(child)

        return data
