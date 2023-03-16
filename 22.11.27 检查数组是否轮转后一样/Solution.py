from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        metanums = sorted(nums)
        n = len(nums)
        count = 0
        res = [ 0 for _ in range(n)]
        while count < n:
            if count == 0:
                transform = nums
            else:
                transform = res
                res = [0 for _ in range(n)]
            for i in range(0,n):
                if i == 0:
                    res[0] = transform[n-1]
                    continue
                res[i] = transform[i-1]
            if res == metanums:
                return True

            count += 1
        return False



nums = [3,4,5,1,2]
solution = Solution()
print(solution.check(nums))