from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 三次遍历
        # n = len(arr)
        #
        # # 左边left[i]为严格小于arr[i]的最近元素位置(不存在时为-1)
        # left = [-1]*n
        # stack = []
        # for i in range(0,n):
        #     while stack and arr[stack[-1]] >= arr[i]:
        #         stack.pop()
        #     if stack:
        #         left[i] = stack[-1]
        #     stack.append(i)
        #
        #
        #
        # # 右边
        # right = [n]*n
        # stack = []
        # for i in range(n-1,-1,-1):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         stack.pop()
        #     if stack:
        #         right[i] = stack[-1]
        #     stack.append(i)




        # 两次遍历

        n = len(arr)
        left,right = [-1]*n,[n]*n
        stack = []
        for i,x in enumerate(arr):
            while stack and arr[stack[-1]] >= x:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)



        ans = 0
        for i,(x,l,r) in enumerate(zip(arr,left,right)):
            ans += x*(i-l)*(r-i)

        return ans % (10**9 +7)






arr = [3,1,2,4]
solution = Solution()
print(solution.sumSubarrayMins(arr))