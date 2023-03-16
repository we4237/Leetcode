from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left=[0]*n
        right=[0]*n
        #遍历单调性
        for i in range(1,n):
            if security[i]<=security[i-1]:#非递增
                left[i] = left[i-1]+1
            if security[n-i-1]<=security[n-i]:#非递减
                right[n-i-1]=right[n-i]+1
        return[i for i in range(time,n-time) if left[i] >= time and right[i] >= time]



if __name__ == '__main__':
    security = [5, 3, 3, 3, 5, 6, 2]
    time = 2
    solution = Solution()
    print(solution.goodDaysToRobBank(security,time))


