from queue import SimpleQueue


class Reader:
    tokens: SimpleQueue

    def __init__(self, filepath):
        self.tokens = SimpleQueue()
        self.token_pointer = 0

        with open(filepath) as file:
            for line in file:
                line = line.split('#', maxsplit=1)[0].strip()

                if line == '':
                    continue

                for token in line.split():
                    self.tokens.put(token)

    def has_token(self) -> bool:
        return not self.tokens.empty()

    def get_token(self) -> str:
        return self.tokens.get()
