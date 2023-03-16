from collections import defaultdict, Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i,x in enumerate(num):
            if int(x) != count[str(i)]:
                return False
        return True

num = "1210"
solution = Solution()
print(solution.digitCount(num))