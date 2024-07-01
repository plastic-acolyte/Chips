from sys import argv
from reader import Reader, Token
from chips import Chips


def main():
    reader = Reader(argv[1])
    chips = Chips()

    while reader.has_token():
        token = reader.get_token()

        match token[0]:
            # Parameterless Commands
            case Token.ADD: chips.add()
            case Token.BANK: chips.bank()
            case Token.EAT: chips.eat()
            case Token.FLIP: chips.flip()
            case Token.NEXT: chips.next()
            case Token.POP: chips.pop()
            case Token.PREV: chips.prev()
            case Token.PUSH: chips.push()
            case Token.SUB: chips.sub()
            case Token.SWAP: chips.swap()
            case Token.WAGER: chips.wager()

            # Commands with one parameter
            case Token.DRAW: handle_draw(chips, reader)


def handle_draw(chips, reader):
    token = reader.get_token()
    chips.draw(token[1])


if __name__ == '__main__':
    main()
