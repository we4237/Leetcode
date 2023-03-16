from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        Max = 100
        line,width = 1,0
        for c in s:
            need =widths[ord(c)-ord('a')]
            width += need
            if width > Max:
                line +=1
                width = need
        return [line,width]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
solution = Solution()
print(solution.numberOfLines(widths,S))
