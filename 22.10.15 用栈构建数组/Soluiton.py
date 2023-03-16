from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        m,i,j = len(target),1,0 # i是压入栈的数字,j为它的指针
        while i <= n  and j < m:
            ans.append('Push')
            if target[j] != i:
                ans.append('Pop')
            else:
                j += 1
            i += 1
        return ans

target = [1,3]
n = 3
solution = Solution()
print(solution.buildArray(target,n))

