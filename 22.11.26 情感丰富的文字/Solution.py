from typing import List

from PIL.ImageOps import expand


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def search(s:str,t:str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    return False
                ch = s[i]
                counti = 0
                while i < len(s) and s[i] == ch:
                    counti += 1
                    i += 1
                countj = 0
                while j < len(t) and t[j] == ch:
                    countj += 1
                    j += 1
                if counti < countj:
                    return False
                if counti != countj and counti < 3:
                    return False
            return i == len(s) and j == len(t)

        return sum(int(search(s,word)) for word in words)

s = "heeellooo"
words = ["hello", "hi", "helo"]
solution = Solution()
print(solution.expressiveWords(s,words))