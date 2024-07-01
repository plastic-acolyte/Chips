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
                case Token.ADD: handle_add(chips, params)
                case Token.BANK: handle_bank(chips, params)
                case Token.DRAW: handle_draw(chips, params)
                case Token.EAT: handle_eat(chips, params)
                case Token.NEXT: handle_pop(chips, params)
                case Token.POP: handle_pop(chips, params)
                case Token.PREV: handle_pop(chips, params)
                case Token.PUSH: handle_push(chips, params)
                case Token.SUB: handle_sub(chips, params)
                case Token.SWAP: handle_swap(chips, params)
                case Token.WAGER: handle_wager(chips, params)
                case _: raise ValueError


def handle_add(chips, params):
    if params:
        raise ValueError

    chips.add()


def handle_bank(chips, params):
    if params:
        raise ValueError

    chips.bank()


def handle_draw(chips, params):
    if not params:
        raise ValueError

    elif not params.isnumeric():
        raise ValueError

    chips.draw(int(params))


def handle_eat(chips, params):
    if params:
        raise ValueError

    chips.eat()


def handle_flip(chips, params):
    if params:
        raise ValueError

    chips.flip()


def handle_next(chips, params):
    if params:
        raise ValueError

    chips.next()


def handle_pop(chips, params):
    if params:
        raise ValueError

    chips.pop()


def handle_prev(chips, params):
    if params:
        raise ValueError

    chips.prev()


def handle_push(chips, params):
    if params:
        raise ValueError

    chips.push()


def handle_sub(chips, params):
    if params:
        raise ValueError

    chips.sub()


def handle_swap(chips, params):
    if params:
        raise ValueError

    chips.swap()


def handle_wager(chips, params):
    if params:
        raise ValueError

    chips.wager()


if __name__ == '__main__':
    main()
