from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        i,n = 0 ,len(s)
        ans = []
        while i < n:
            if s[i] == '(':
                j = s.find(')',i+1)
                ans.append(d.get(s[i+1:j],'?'))
                i = j
            else:
                ans.append(s[i])
            i += 1
        return ''.join(ans)

s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
solution = Solution()
print(solution.evaluate(s,knowledge))