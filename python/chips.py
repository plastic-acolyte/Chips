from typing import Optional
from stack import Stack

NUM_STACKS = 777
STARTING_BANK = 1000

MIN_WAGER = 10
MAX_WAGER = 1_000_000


class Chips:
    memory: [Stack]
    stack_pointer: int
    active_chip: Optional[float]
    bank: float

    def __init__(self):
        self.memory = [Stack() for _ in range(NUM_STACKS)]
        self.stack_pointer = 0
        self.active_chip = None
        self.bank = STARTING_BANK

    def eat(self, mode):
        pass

    def put(self, value):
        pass
