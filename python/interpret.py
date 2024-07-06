from sys import argv

from chips import Chips
from error import *
from parse import *


class ChipsInterpreter:
    chips: Chips

    def __init__(self):
        self.reset()

    def reset(self):
        self.chips = Chips()

    def run(self, filepath):
        parser = Parser(filepath)

        while parser.has_next():
            data = parser.next()

            try:
                self.interpret(data)

            except (BankError, HandError) as err:
                print("Error at command {} on line {}:".format(data.token.value.name, data.token.line_number))

                if isinstance(err, BankError):
                    print("\tBank is overdrawn")

                elif isinstance(err, HandError):
                    if self.chips.hand is None:
                        print("\tNot holding a chip")
                    else:
                        print("\tAlready holding a chip")

                return

    def interpret(self, data: CommandData) -> None:
        match data.token.value:
            case Command.ADD:
                self.chips.add()

            case Command.BANK:
                self.chips.bank()

            case Command.DRAW:
                self.handle_draw(data)

            case Command.EAT:
                self.chips.eat()

            case Command.FLIP:
                self.chips.flip()

            case Command.NEXT:
                self.chips.next()

            case Command.POP:
                self.chips.pop()

            case Command.PREV:
                self.chips.prev()

            case Command.PUSH:
                self.chips.push()

            case Command.SUB:
                self.chips.sub()

            case Command.SWAP:
                self.chips.swap()

            case Command.WAGER:
                self.chips.wager()

            case Command.WHILE:
                self.handle_while(data)

    def handle_draw(self, data: CommandData) -> None:
        self.chips.draw(data.parameters[0].value)

    def handle_while(self, data: CommandData) -> None:
        while self.is_not_zero(data.parameters[0].value):
            for child in data.children:
                self.interpret(child)

    def is_not_zero(self, register: Register) -> bool:
        if register == Register.HAND:
            return not self.chips.peek_hand() == 0

        elif register == Register.TOP:
            return not self.chips.peek_top() == 0


if __name__ == '__main__':
    ChipsInterpreter().run(argv[1])
