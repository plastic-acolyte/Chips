from enum import Enum
from random import randint
from typing import Optional

from error import *
from stack import Stack
from token import Token

NUM_STACKS = 777
STARTING_BANK = 777


class Chips:
    memory: [Stack]
    stack_pointer: int
    hand: Optional[int]
    balance: int

    def __init__(self):
        self.memory = [Stack() for _ in range(NUM_STACKS)]
        self.stack_pointer = 0
        self.hand = None
        self.balance = STARTING_BANK

    def add(self):
        if not self.hand:
            raise HandError(Token.ADD.value, False)

        self.hand += self.memory[self.stack_pointer].pop()

    def bank(self):
        if not self.hand:
            raise HandError(Token.BANK.value, False)

        self.balance += abs(self.hand)
        self.hand = None

    def draw(self, value):
        if self.balance < abs(value):
            raise BankError

        if self.hand:
            raise HandError(Token.DRAW.value, True)

        self.hand = value
        self.balance -= abs(value)

    def eat(self):
        if not self.hand:
            raise HandError(Token.EAT.value, False)

        print(chr(self.hand), end='')
        self.hand = None

    def flip(self):
        if not self.hand:
            raise HandError(Token.FLIP.value, False)

        self.hand = -self.hand

    def next(self):
        self.stack_pointer = (self.stack_pointer + 1) % NUM_STACKS

    def pop(self):
        if self.hand:
            raise HandError(Token.POP.value, True)

        self.hand = self.memory[self.stack_pointer].pop()

    def prev(self):
        self.stack_pointer = (self.stack_pointer - 1) % NUM_STACKS

    def push(self):
        if not self.hand:
            raise HandError(Token.PUSH.value, False)

        self.memory[self.stack_pointer].push(self.hand)
        self.hand = None

    def sub(self):
        if not self.hand:
            raise HandError(Token.SUB.value, False)

        self.hand -= self.memory[self.stack_pointer].pop()

    def swap(self):
        if not self.hand:
            raise HandError(Token.SWAP.value, False)

        top = self.memory[self.stack_pointer].pop()
        self.memory[self.stack_pointer].push(self.hand)
        self.hand = top

    def wager(self):
        if not self.hand:
            raise HandError(Token.WAGER.value, False)

        sevens = 0

        for _ in range(3):
            if randint(1, 7) == 7:
                sevens += 1

        match sevens:
            case 1: self.balance += self.hand * 2
            case 2: self.balance += self.hand * 7
            case 3: self.balance += self.hand * 777

        self.hand = None
