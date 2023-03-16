from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s:str,t:str)->bool:
            pt_s=pt_t=0
            while pt_s<len(s) and pt_t<len(t):
                if s[pt_s]==t[pt_t]:
                    pt_s+=1
                pt_t+=1
            return pt_s==len(s)

        ans = -1
        for i,s in enumerate(strs):
            check = True
            for j,t in enumerate(strs):
                if i != j and is_subseq(s,t):
                    check = False
                    break
            if check != False:
                ans = max(ans,len(s))
        return ans

strs = ["aba","cdc","eae"]
solution=Solution()
print(solution.findLUSlength(strs))