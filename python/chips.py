from enum import Enum
from typing import Optional

from error import *
from stack import Stack

NUM_STACKS = 777
STARTING_BANK = 777


class Command(Enum):
    ADD = "ADD"
    BANK = "BANK"
    DRAW = "DRAW"
    EAT = "EAT"
    FLIP = "FLIP"
    POP = "POP"
    PUSH = "PUSH"
    SUB = "SUB"
    SWAP = "SWAP"

    @staticmethod
    def parse(value):
        match value:
            case "ADD": return Command.ADD
            case "BANK": return Command.BANK
            case "DRAW": return Command.DRAW
            case "EAT": return Command.EAT
            case "FLIP": return Command.FLIP
            case "POP": return Command.POP
            case "PUSH": return Command.PUSH
            case "SUB": return Command.SUB
            case "SWAP": return Command.SWAP


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

    def add(self):
        if not self.hand:
            raise HandError(Command.ADD.value, False)

        self.hand += self.memory[self.stack_pointer].pop()

    def bank(self):
        if not self.hand:
            raise HandError(Command.BANK.value, False)

        self.bank += abs(self.hand)
        self.hand = None

    def draw(self, value):
        if self.bank < abs(value):
            raise BankError

        if self.hand:
            raise HandError(Command.DRAW.value, True)

        self.hand = value
        self.bank -= abs(value)

    def eat(self):
        if not self.hand:
            raise HandError(Command.EAT.value, False)

        print(chr(self.hand), end='')
        self.hand = None

    def flip(self):
        if not self.hand:
            raise HandError(Command.FLIP.value, False)

        self.hand = -self.hand

    def pop(self):
        if self.hand:
            raise HandError(Command.POP.value, True)

        self.hand = self.memory[self.stack_pointer].pop()

    def push(self):
        if not self.hand:
            raise HandError(Command.PUSH.value, False)

        self.memory[self.stack_pointer].push(self.hand)
        self.hand = None

    def sub(self):
        if not self.hand:
            raise HandError(Command.SUB.value, False)

        self.hand -= self.memory[self.stack_pointer].pop()

    def swap(self):
        if not self.hand:
            raise HandError(Command.SWAP.value, False)

        top = self.memory[self.stack_pointer].pop()
        self.memory[self.stack_pointer].push(self.hand)
        self.hand = top
