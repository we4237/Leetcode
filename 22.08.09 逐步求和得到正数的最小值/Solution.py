from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sumMin,sum = 0,0
        for num in nums:
            sum += num
            sumMin = min(sum,sumMin)
        return 1-sumMin