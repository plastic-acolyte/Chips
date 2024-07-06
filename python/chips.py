from random import randint
from typing import Optional
from collections import deque

from error import *
from parse import Command

NUM_STACKS = 777
STARTING_BANK = 777


class Chips:
    memory: [deque]
    stack_pointer: int
    hand: Optional[int]
    balance: int

    def __init__(self):
        self.memory = [deque() for _ in range(NUM_STACKS)]
        self.stack_pointer = 0
        self.hand = None
        self.balance = STARTING_BANK

    def add(self):
        if self.hand is None:
            raise HandError(Command.ADD.name, False)

        self.hand += self.memory[self.stack_pointer].pop()

    def bank(self):
        if self.hand is None:
            raise HandError(Command.BANK.name, False)

        self.balance += abs(self.hand)
        self.hand = None

    def draw(self, value):
        if self.balance < abs(value):
            raise BankError

        if self.hand is not None:
            raise HandError(Command.DRAW.name, True)

        self.hand = value
        self.balance -= abs(value)

    def eat(self):
        if self.hand is None:
            raise HandError(Command.EAT.name, False)

        print(chr(self.hand), end='')
        self.hand = None

    def flip(self):
        if self.hand is None:
            raise HandError(Command.FLIP.name, False)

        self.hand = -self.hand

    def next(self):
        self.stack_pointer = (self.stack_pointer + 1) % NUM_STACKS

    def peek_hand(self):
        return self.hand

    def peek_top(self):
        return self.memory[self.stack_pointer][-1]

    def pop(self):
        if self.hand is not None:
            raise HandError(Command.POP.name, True)

        self.hand = self.memory[self.stack_pointer].pop()

    def prev(self):
        self.stack_pointer = (self.stack_pointer - 1) % NUM_STACKS

    def push(self):
        if self.hand is None:
            raise HandError(Command.PUSH.name, False)

        self.memory[self.stack_pointer].append(self.hand)
        self.hand = None

    def sub(self):
        if self.hand is None:
            raise HandError(Command.SUB.name, False)

        self.hand -= self.memory[self.stack_pointer].pop()

    def swap(self):
        if self.hand is None:
            raise HandError(Command.SWAP.name, False)

        top = self.memory[self.stack_pointer].pop()
        self.memory[self.stack_pointer].append(self.hand)
        self.hand = top

    def wager(self):
        if self.hand is None:
            raise HandError(Command.WAGER.name, False)

        sevens = 0

        for _ in range(3):
            if randint(1, 7) == 7:
                sevens += 1

        match sevens:
            case 1: self.balance += self.hand * 2
            case 2: self.balance += self.hand * 7
            case 3: self.balance += self.hand * 777

        self.hand = None
