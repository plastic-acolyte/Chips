from sys import argv
from chips import Chips
from enum import Enum, auto


class Command(Enum):
    EAT = auto()
    PUT = auto()

    @staticmethod
    def parse(value):
        match value:
            case "EAT": return Command.EAT
            case "PUT": return Command.PUT


def main():
    chips = Chips()

    with open(argv[1]) as file:
        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue

            pieces = line.strip().split(maxsplit=1)
            cmd = Command.parse(pieces[0])
            params = pieces[1] if len(pieces) > 1 else ""

            match cmd:
                case Command.EAT: handle_eat(chips, params)
                case Command.PUT: handle_put(chips, params)
                case _: raise ValueError


def handle_eat(chips, params):
    if params == '' or params == 'C':
        chips.eat()
    elif params == 'N':
        chips.eat('N')
    else:
        raise ValueError


def handle_put(chips, params):
    if params == '':
        chips.put()
    elif params.isnumeric():
        chips.put()
    else:
        raise ValueError


if __name__ == '__main__':
    main()
