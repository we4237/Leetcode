from collections import Counter
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:

        res = 0
        while sum(amount):
            amount.sort()
            amount[2] -= 1
            amount[1] = max(0,amount[1]-1)
            res += 1
        return res







amount = [5,4,4]
solution = Solution()
print(solution.fillCups(amount))