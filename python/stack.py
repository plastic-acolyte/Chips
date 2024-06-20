class Stack:
    contents: [int]

    def __init__(self) -> None:
        self.contents = []

    def pop(self) -> int:
        return self.contents.pop()

    def push(self, value) -> None:
        self.contents.append(value)

    def eat_as_char(self) -> str:
        result = ""

        for value in self.contents:
            result += chr(value)

        self.contents = []
        return result

    def eat_as_num(self) -> int:
        result = 0

        for value in self.contents:
            result += value

        self.contents = []
        return result
