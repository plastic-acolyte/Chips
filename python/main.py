from sys import argv

from chips import Chips
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
        interpret(chips, data)


def interpret(chips: Chips, data: CommandData) -> None:
    match data.token.value:
        case Command.ADD:
            chips.add()

        case Command.BANK:
            chips.bank()

        case Command.DRAW:
            chips.draw(data.parameters[0].value)

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


if __name__ == '__main__':
    main()
