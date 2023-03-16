from bisect import bisect_right
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]

letters = ["c", "f", "j"]
target = "d"
solution =Solution()
print(solution.nextGreatestLetter(letters,target))
