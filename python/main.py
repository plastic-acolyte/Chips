from sys import argv
from chips import Chips
from token import Token


def main():
    chips = Chips()

    with open(argv[1]) as file:
        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue

            pieces = line.strip().split(maxsplit=1)
            cmd = Token.parse(pieces[0])
            params = pieces[1] if len(pieces) > 1 else None

            match cmd:
                case Token.ADD: chips.add()
                case Token.BANK: chips.bank()
                case Token.DRAW: handle_draw(chips, params)
                case Token.EAT: chips.eat()
                case Token.FLIP: chips.flip()
                case Token.NEXT: chips.next()
                case Token.POP: chips.pop()
                case Token.PREV: chips.prev()
                case Token.PUSH: chips.push()
                case Token.SUB: chips.sub()
                case Token.SWAP: chips.swap()
                case Token.WAGER: chips.wager()
                case _: raise ValueError


def handle_draw(chips, params):
    if not params:
        raise ValueError

    elif not params.isnumeric():
        raise ValueError

    chips.draw(int(params))


if __name__ == '__main__':
    main()
