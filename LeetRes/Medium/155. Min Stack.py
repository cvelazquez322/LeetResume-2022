class MinStack:
    def __init__(self):
        self.array = []
        self.minimum = 0
            def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.minimum = val
        else:
            self.minimum = min(self.minimum, val)
                self.array.append(val)
            def pop(self) -> None:
        if self.minimum == self.array[-1]:
            del self.array[-1]
            if len(self.array) >= 1:
                self.minimum = min(self.array)
            else:
                self.minimum = 0
        else:
            del self.array[-1]
            def top(self) -> int:
        return self.array[-1]
            def getMin(self) -> int:
        return self.minimum
        # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()