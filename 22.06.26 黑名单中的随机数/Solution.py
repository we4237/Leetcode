import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.whitelist_num = n -len(blacklist)
        last = n-1

        self.n = n
        self.mapping = {}
        #下面这步是为了更快判断last是否在blacklist里
        for b in blacklist:
            self.mapping[b]=666
        for b in blacklist:
            if b>=self.whitelist_num:
                continue
            while last in self.mapping:
                last -= 1
            self.mapping[b]=last
            last-=1

    def pick(self) -> int:
        index = random.randrange(self.whitelist_num)
        if index in self.mapping:
            return self.mapping[index]
        return index



# Your Solution object will be instantiated and called as such:
n= 7
blacklist=[2,3,5]
obj = Solution(n, blacklist)
param_1 = obj.pick()
print(param_1)