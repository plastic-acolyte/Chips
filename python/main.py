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

            match cmd:
                case Command.EAT: handle_eat(chips, pieces[1])
                case Command.PUT: handle_put(chips, pieces[1])
                case _: raise ValueError


def handle_eat(chips, param_string):
    pass


def handle_put(chips, param_string):
    pass


if __name__ == '__main__':
    main()
