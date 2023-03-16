from collections import Counter
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt = cnt.most_common()
        return cnt[0][0]