from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = n = len(s)
        perm =[0]*(n+1)
        for i,ch in enumerate(s):
            if ch == 'I':
                perm[i]=lo
                lo+=1
            if ch == 'D':
                perm[i]=hi
                hi-=1
        perm[n] = lo
        return perm

s = "IDID"
solution= Solution()
print(solution.diStringMatch(s))