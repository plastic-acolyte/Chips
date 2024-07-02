from sys import argv
from chips import Chips
from tokenizer import *


def main():
    tokenizer = Tokenizer(argv[1])
    chips = Chips()

    while tokenizer.has_next():
        token = tokenizer.next()

        if not token.type == TokenType.COMMAND:
            raise ValueError

        match token.value:
            # Parameterless Commands
            case Command.ADD:
                chips.add()
            case Command.BANK:
                chips.bank()
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

            # Commands with one parameter
            case Command.DRAW:
                handle_draw(chips, tokenizer)

            # Block commands
            case Command.WHILE:
                handle_while(chips, tokenizer)


def handle_draw(chips, tokenizer):
    token = tokenizer.next()

    if not token.type == TokenType.INT:
        raise ValueError

    chips.draw(token.value)


def handle_while(chips, tokenizer):
    pass


if __name__ == '__main__':
    main()
