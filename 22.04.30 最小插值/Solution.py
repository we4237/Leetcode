from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxn = max(nums)
        minn = min(nums)
        if maxn - minn <= 2*k:
            return 0
        else:
            return(maxn - minn - 2*k)
