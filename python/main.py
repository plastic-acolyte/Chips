from sys import argv

if __name__ == '__main__':
    with open(argv[1]) as file:
        for line in file:
            print(line.strip())
