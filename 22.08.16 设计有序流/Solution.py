from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = ['']*(n+1)
        self.ptr = 1 # 从1开始的指针


    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream
        stream_[idKey] = value
        res = list()
        while self.ptr <len(stream_) and self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr +=1
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)