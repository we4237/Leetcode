class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1 )//2
            if self.valid(mid,n,index,maxSum):
                left = mid
            else:
                right = mid - 1
        return left

    def valid(self,mid:int,n:int,index:int,maxSum:int) -> bool:
        left = index
        right = n - index - 1
        return mid + self.cal(mid,left) + self.cal(mid,right) <= maxSum

    def cal(self,big:int,length:int) -> int:
        if length + 1 < big:
            small = big - length
            return ((big - 1 + small) * length)//2
        else:
            ones = length -(big - 1)
            return (big - 1 + 1)*(big - 1) // 2 +ones

n = 4
index = 2
maxSum = 6
solution = Solution()
print(solution.maxValue(n,index,maxSum))