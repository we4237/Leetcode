import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minvaluestack = [math.inf]
        self.mystack = []

    def push(self, x: int) -> None:
        if self.minvaluestack[-1] >= x:
            self.minvaluestack.append(x)
        else:
            self.minvaluestack.append(self.minvaluestack[-1])
        self.mystack.append(x)


    def pop(self) -> None:
        self.mystack.pop()
        self.minvaluestack.pop()


    def top(self) -> int:
        return self.mystack[-1]

    def min(self) -> int:
        return self.minvaluestack[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()