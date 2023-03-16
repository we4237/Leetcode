from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph:str, banned: List[str]) -> str:
        # 建立哈希表
        ban = set(banned)

        freq = Counter()

        word,n="",len(paragraph)
        for i in range(1+n):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in ban:
                    freq[word] += 1
                word = ""
        maxfre = max(freq.values())
        return next(word for word,f in freq.items() if f == maxfre)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
solution = Solution()
print(solution.mostCommonWord(paragraph,banned))