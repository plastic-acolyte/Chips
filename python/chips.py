from enum import Enum
from random import randint
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
            case "ADD": return Command.ADD
            case "BANK": return Command.BANK
            case "DRAW": return Command.DRAW
            case "EAT": return Command.EAT
            case "FLIP": return Command.FLIP
            case "NEXT": return Command.NEXT
            case "POP": return Command.POP
            case "PREV": return Command.PREV
            case "PUSH": return Command.PUSH
            case "SUB": return Command.SUB
            case "SWAP": return Command.SWAP
            case "WAGER": return Command.WAGER


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

    def next(self):
        self.stack_pointer = (self.stack_pointer + 1) % NUM_STACKS

    def pop(self):
        if self.hand:
            raise HandError(Command.POP.value, True)

        self.hand = self.memory[self.stack_pointer].pop()

    def prev(self):
        self.stack_pointer = (self.stack_pointer - 1) % NUM_STACKS

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

    def wager(self):
        if not self.hand:
            raise HandError(Command.WAGER.value, False)

        sevens = 0

        for _ in range(3):
            if randint(1, 7) == 7:
                sevens += 1

        match sevens:
            case 1: self.bank += self.hand * 2
            case 2: self.bank += self.hand * 7
            case 3: self.bank += self.hand * 777

        self.hand = None
