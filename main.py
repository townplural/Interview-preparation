class Stack:
    def __init__(self, string: str):
        self.string = string

    def is_empty(self) -> bool:
        if self.string is None:
            return True
        return False

    def push(self, item: object):
        self.string += item

    def pop(self):
        poped_item = self.string[-1]
        self.string = self.string[:-1]
        return poped_item

    def peek(self):
        return self.string[-1]

    def size(self):
        print(self.string)
        return len(self.string)

    def task_2(self):
        if len(self.string) % 2 != 0:
            return False


if __name__ == '__main__':
    st = Stack('123')
    stringqq = '(((([{}]))))'


