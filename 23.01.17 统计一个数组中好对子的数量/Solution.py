from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = Counter()
        res = 0
        for i in nums:
            j = int(str(i)[::-1])
            res += cnt[i - j]
            cnt[i - j] += 1
        return res % (10 ** 9 + 7)


nums = [13,10,35,24,76]
solution = Solution()
print(solution.countNicePairs(nums))