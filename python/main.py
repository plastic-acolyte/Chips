from sys import argv

from chips import Chips
from error import *
from parse import *


def is_not_zero(chips: Chips, register: Register) -> bool:
    if register == Register.HAND:
        return not chips.peek_hand() == 0

    elif register == Register.TOP:
        return not chips.peek_top() == 0


def main():
    parser = Parser(argv[1])
    chips = Chips()

    while parser.has_next():
        data = parser.next()

        try:
            interpret(chips, data)

        except (BankError, HandError) as err:
            print("Error at command {} on line {}:".format(data.token.value.name, data.token.line_number))

            if isinstance(err, BankError):
                print("\tBank is overdrawn")

            elif isinstance(err, HandError):
                if chips.hand is None:
                    print("\tNot holding a chip")
                else:
                    print("\tAlready holding a chip")

            return


def interpret(chips: Chips, data: CommandData) -> None:
    match data.token.value:
        case Command.ADD:
            chips.add()

        case Command.BANK:
            chips.bank()

        case Command.DRAW:
            handle_draw(chips, data)

        case Command.EAT:
            chips.eat()

        case Command.FLIP:
            chips.flip()

        case Command.NEXT:
            chips.next()

        case Command.POP:
            chips.pop()

        case Command.PREV:
            chips.prev()

        case Command.PUSH:
            chips.push()

        case Command.SUB:
            chips.sub()

        case Command.SWAP:
            chips.swap()

        case Command.WAGER:
            chips.wager()

        case Command.WHILE:
            handle_while(chips, data)


def handle_draw(chips: Chips, data: CommandData) -> None:
    chips.draw(data.parameters[0].value)


def handle_while(chips: Chips, data: CommandData) -> None:
    while is_not_zero(chips, data.parameters[0].value):
        for child in data.children:
            interpret(chips, child)


if __name__ == '__main__':
    main()
