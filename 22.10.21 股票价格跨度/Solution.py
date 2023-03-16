class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        t = 1
        while self.stack and self.stack[-1][0] <= price:
            t += self.stack.pop()[1]
        self.stack.append((price,t))
        return t


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
print('param_1:'+str(param_1))
param_2 = obj.next(80)
print('param_2:'+str(param_2))
param_3 = obj.next(90)
print('param_3:'+str(param_3))