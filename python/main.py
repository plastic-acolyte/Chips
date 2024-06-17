from sys import argv
from stack import Stack


def main():
    memory = [Stack() for _ in range(777)]
    stack_pointer = 0
    active_chip = None

    with open(argv[1]) as file:
        for line in file:
            print(line.strip())


if __name__ == '__main__':
    main()

