from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0]*(n+1)
        for i,num in enumerate(nums):
            if i >= num:
                diff[0] += 1
                diff[i-num+1] -= 1
                diff[i +1] += 1
            else:
                diff[i+1]+=1
                diff[i-num+n+1]-=1
        ans = cur = mx =0
        for i in range(n):
                cur += diff[i]
                if cur > mx:
                    ans,mx = i ,cur
        return ans






if __name__ =='__main__':
    nums = [2, 3, 1, 4, 0]
    solution = Solution()
    print(solution.bestRotation(nums))
