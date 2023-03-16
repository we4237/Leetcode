from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[1])
        f = [0]*(n+10)
        for i in range(1,n+1):
            start,end,money = jobs[i - 1]
            f[i] = max(f[i-1],money) # 开始判断前赚的钱
            l,r = 0,i-1
            while l < r:

                mid = l+r+1 >> 1
                if jobs[mid][1] <= start:
                    l = mid
                else:
                    r = mid - 1

                if jobs[r][1] <= start:
                    f[i] = max(f[i],f[r+1]+money)
        return f[n]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
solution = Solution()
print(solution.jobScheduling(startTime,endTime,profit))


