from sys import argv
from chips import Chips, Command


def main():
    chips = Chips()

    with open(argv[1]) as file:
        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue

            pieces = line.strip().split(maxsplit=1)
            cmd = Command.parse(pieces[0])
            params = pieces[1] if len(pieces) > 1 else None

            match cmd:
                case Command.ADD: handle_add(chips, params)
                case Command.BANK: handle_bank(chips, params)
                case Command.DRAW: handle_draw(chips, params)
                case Command.EAT: handle_eat(chips, params)
                case Command.POP: handle_pop(chips, params)
                case Command.PUSH: handle_push(chips, params)
                case Command.SUB: handle_sub(chips, params)
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


def handle_pop(chips, params):
    if params:
        raise ValueError

    chips.pop()


def handle_push(chips, params):
    if params:
        raise ValueError

    chips.push()


def handle_sub(chips, params):
    if params:
        raise ValueError

    chips.sub()


if __name__ == '__main__':
    main()
