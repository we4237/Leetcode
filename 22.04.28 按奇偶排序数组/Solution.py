from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return [num for num in nums if num % 2 == 0]+[num for num in nums if num %  2 == 1]
        n = len(nums)
        left,right = 0, n-1
        res = [0]*n
        for num in nums:
            if num %2 == 0:
                res[left]=num
                left += 1
            else:
                res[right]=num
                right -=1
        return res

nums  = [3,1,2,4]
solution = Solution()
print(solution.sortArrayByParity(nums))