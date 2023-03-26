from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ji = []
        ou = []
        for x in nums:
            if x % 2 == 0:
                ou.append(x)
            else:
                ji.append(x)

        ans = ji+ou
        return ans


nums = [1,2,3,4]
solution = Solution()
print(
    solution.exchange(nums)
)