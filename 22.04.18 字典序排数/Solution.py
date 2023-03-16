from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # def dfs(cur,n,res):
        #     if cur>n:return
        #     res.append(cur)
        #     for i in range(0,10):
        #         dfs(cur*10+i,n,res)
        #
        # res = []
        # for i in range(1,10):
        #     dfs(i,n,res)
        # return res
        ans = [0]*n
        num = 1
        for i in range(n):
            ans[i] = num
            if num*10 <= n:
                num *=10
            else:
                while num % 10 == 9 or num + 1>n:
                    num //=10
                num +=1
        return ans


n=13
solution = Solution()
print(solution.lexicalOrder(n))