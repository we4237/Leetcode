from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1)
        b = ''.join(word2)
        return True if a == b else False

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
solution = Solution()
print(solution.arrayStringsAreEqual(word1,word2))