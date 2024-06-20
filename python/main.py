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
                case Command.DRAW: handle_draw(chips, params)
                case Command.EAT: handle_eat(chips, params)
                case Command.PUSH: handle_push(chips, params)
                case _: raise ValueError


def handle_draw(chips, params):
    if not params:
        raise ValueError

    elif not params.isnumeric():
        raise ValueError

    chips.draw(int(params))


def handle_eat(chips, params):
    if params == '' or params == 'C':
        chips.eat()
    elif params == 'N':
        chips.eat('N')
    else:
        raise ValueError


def handle_push(chips, params):
    if params:
        raise ValueError

    chips.push()


if __name__ == '__main__':
    main()
