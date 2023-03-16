from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res,visited = set(),set()
        for num in nums:
            if num - k in visited:
                res.add(num-k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)

nums = [3, 1, 4, 1, 5]
k = 2
solution=Solution()
print(solution.findPairs(nums,k))