from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        color = Counter(suits)
        number = Counter(ranks)
        n = 5
        ans = ""
        if len(color) == 1:
            ans = "Flush"
            return ans
        if len(number) == 5:
            ans = "High Card"
            return ans
        for x in number.values():
            if x >= 3:
                ans = "Three of a Kind"
                break
            if x == 2:
                ans = "Pair"
        return ans



ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]
solution = Solution()
print(solution.bestHand(ranks,suits))