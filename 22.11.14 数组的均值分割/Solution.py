from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        for i,v in enumerate(nums):
            nums[i] = v*n - s
        # 二进制枚举

        m = n // 2
        # 哈希表
        vis = set()
        # 折半查找
        for i in range(1,1<<m):
            t = sum(v for j,v in enumerate(nums[:m]) if i >> j & 1)
            if t == 0:
                return True
            vis.add(t)
        rsum = sum(nums[m:])
        for i in range(1,1<<(n-m)):
            t = sum(v for j,v in enumerate(nums[m:]) if i >> j & 1)
            if t == 0 or rsum != t and -t in vis:
                return True
        return False

nums = [1,2,3,4,5,6,7,8]
solution = Solution()
print(solution.splitArraySameAverage(nums))