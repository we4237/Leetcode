from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        left = ans = 0
        for right,x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt)>2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans,right-left+1)
        return ans

fruits = [1,2,1]
solution=Solution()
print(solution.totalFruit(fruits))