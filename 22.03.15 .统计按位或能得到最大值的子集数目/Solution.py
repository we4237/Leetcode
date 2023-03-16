from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n =len(nums)
        maxOr,cnt=0,0
        for i in range(1,1<<n):
            orVal = reduce(or_,(num for j,num in enumerate(nums) if (i>>j)&1 == 1),0)
            if maxOr<orVal:
                maxOr = orVal
                cnt = 1
            elif maxOr == orVal:
                cnt+=1
        return cnt

if __name__ =='__main__':
    nums = [3, 1]
    solution = Solution()
    print(solution.countMaxOrSubsets(nums))