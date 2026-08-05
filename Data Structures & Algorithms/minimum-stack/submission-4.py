class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:   #add value
        self.stack.append(val)

        current_min = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(current_min)

    def pop(self) -> None: #remove top value
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int: #return top value
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]