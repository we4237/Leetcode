from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for column in zip(*strs):
            if list(column) != sorted(column):
                res +=1
        return len(strs[0])-res

strs = ["cba","daf","ghi"]
solution = Solution()
solution.minDeletionSize(strs)