from enum import Enum
from typing import Optional

from error import *
from stack import Stack

NUM_STACKS = 777
STARTING_BANK = 777


class Command(Enum):
    BANK = "BANK"
    DRAW = "DRAW"
    EAT = "EAT"
    PUSH = "PUSH"

    @staticmethod
    def parse(value):
        match value:
            case "BANK": return Command.BANK
            case "DRAW": return Command.DRAW
            case "EAT": return Command.EAT
            case "PUSH": return Command.PUSH


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
            raise HandError(Command.DRAW.value, True)

        self.hand = value
        self.bank -= abs(value)

    def eat(self, mode='C'):
        pass

    def push(self):
        if not self.hand:
            raise HandError(Command.PUSH.value, False)
