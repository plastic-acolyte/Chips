from enum import Enum, auto
from typing import Optional

from error import *
from stack import Stack

NUM_STACKS = 777
STARTING_BANK = 777


class Command(Enum):
    BANK = auto()
    DRAW = auto()
    EAT = auto()
    PUT = auto()

    @staticmethod
    def parse(value):
        match value:
            case "BANK": return Command.BANK
            case "DRAW": return Command.DRAW
            case "EAT": return Command.EAT
            case "PUT": return Command.PUT


class Chips:
    memory: [Stack]
    stack_pointer: int
    hand: Optional[int]
    bank: int

    def __init__(self):
        self.memory = [Stack() for _ in range(NUM_STACKS)]
        self.stack_pointer = 0
        self.hand = None
        self.bank = STARTING_BANK

    def draw(self, value):
        if self.bank < abs(value):
            raise BankError

        if self.hand:
            raise HandError("DRAW", True)

        self.hand = value
        self.bank -= abs(value)

    def eat(self, mode='C'):
        pass

    def put(self):
        if not self.hand:
            raise HandError("PUT", False)
