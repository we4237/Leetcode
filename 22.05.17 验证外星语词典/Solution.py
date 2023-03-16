
from typing import List

from nltk import pairwise


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c:i for i,c in enumerate(order)}
        return all( s<=t for s,t in pairwise([index[c] for c in word] for word in words) )

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
solution= Solution()
print(solution.isAlienSorted(words,order))