class Stack:
    contents: [int]

    def __init__(self) -> None:
        self.contents = []

    def pop(self) -> int:
        return self.contents.pop()

    def push(self, value: int) -> None:
        self.contents.append(value)
