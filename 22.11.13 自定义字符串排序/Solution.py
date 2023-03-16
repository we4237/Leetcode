from collections import defaultdict

import numpy as np
from numpy import char


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        val = defaultdict(int)
        for i, ch in enumerate(order):
            val[ch] = i + 1

        return ''.join(sorted(s , key=lambda ch : val[ch]))


order = "cbafg"
s = "abcd"
solution = Solution()
print(solution.customSortString(order,s))