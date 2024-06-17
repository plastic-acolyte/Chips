class Stack:
    contents: [float]

    def __init__(self):
        self.contents = []

    def put(self, value):
        self.contents.append(value)

    def eat_as_char(self) -> str:
        result = ""

        for value in self.contents:
            result += chr(value)

        self.contents = []
        return result

    def eat_as_num(self) -> float:
        result = 0

        for value in self.contents:
            result += value

        self.contents = []
        return result
