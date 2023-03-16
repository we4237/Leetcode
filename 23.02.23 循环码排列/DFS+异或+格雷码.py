from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:


        visited = [0 for i in range(2 ** n)]
        nums = [start]
        stack = []
        res = []
        flags = [True]

        def dfs(nums,stack,visited,start,cen,n,flags):

            if not flags[0]:
                return

            cur_nums = []

            # 终止条件
            if not nums and cen<=2**n:
                return
            if cen == 2**n+1:
                flag = 1
                last = stack[-1]
                for i in range(0,n):
                    if last ^ (1<<i) == start:
                        #用异或就行，将数分别于10,100,1000。。异或的得到的数就是他的相差一位的数
                        flag = 0
                        res.append(stack[:])
                        break
                if flag == 0:
                    flags[0] = False
                return


            for num in nums:
                visited[num] = 1
                stack.append(num)
                for i in range(0,n):
                    nextnum = num^(1<<i)
                    if visited[nextnum] == 0:
                        cur_nums.append(nextnum)
                    dfs(cur_nums,stack,visited,start,cen+1,n,flags)
                stack.pop()
                visited[num] = 0

        dfs(nums,stack,visited,start,1,n,flags)

        return res[0]

n = 2
start = 3
solution = Solution()
print(solution.circularPermutation(n,start))

