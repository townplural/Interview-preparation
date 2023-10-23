class Stack:
    def __init__(self, string: str):
        self.string = string

    def is_empty(self) -> bool:
        if self.string is None:
            return True
        return False

    def push(self, item: object):
        self.string += item

    def pop(self) -> str:
        poped_item = self.string[-1]
        self.string = self.string[:-1]
        return poped_item

    def peek(self) -> str:
        return self.string[-1]

    def size(self) -> int:
        return len(self.string)

    def task_2(self) -> bool:
        ans = 0

        if len(self.string) % 2 != 0:
            return False
        dict1 = {}
        for i in range(len(self.string)):
            if self.string[i] not in dict1:
                dict1[self.string[i]] = 0
            dict1[self.string[i]] += 1
        for key, value in dict1.items():
            if '(' in self.string and key == '(' and value != dict1[')']:
                ans += 1
            if '[' in self.string and key == '[' and value != dict1[']']:
                ans += 1
            if '{' in self.string and key == '{' and value != dict1['}']:
                ans += 1
        if ans >= 1:
            return False
        return True

        




if __name__ == '__main__':
    string1 = '(((([{}]))))'
    string2 = '[([])((([[[]]])))]{()}'
    string3 = '{{[()]}}'
    string4 = '}{}'
    string5 = '{{[(])]}}'
    string6 = '[[{())}]'
    string = ''

    st = Stack(input())
    print(st.task_2())
