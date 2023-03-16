from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_word = [f'{x}' for x in allowed]
        level_1 = []

        for word in words:
            i = 0
            while i < len(word):
                # for i,c in enumerate(word):
                if word[i] in allowed:
                    i += 1
                else:
                    break

                if i == len(word) :
                    level_1.append(word)
                    break






        return len(level_1)

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
solution = Solution()
print(solution.countConsistentStrings(allowed,words))