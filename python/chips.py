from typing import Optional
from stack import Stack

NUM_STACKS = 777
STARTING_BANK = 777


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

    def eat(self, mode='C'):
        pass

    def put(self, value=0):
        pass
