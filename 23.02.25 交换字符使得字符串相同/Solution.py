class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x1y2 , y1x2 = 0,0
        for a,b in zip(s1,s2):
            x1y2 += a<b
            y1x2 += a>b
        if (x1y2 + y1x2) % 2 == 1:
            return -1
        else:
            return (x1y2) // 2+ (y1x2) // 2 + x1y2 % 2 + y1x2 % 2

s1 = "xy"
s2 = "yx"
solution = Solution()
print(solution.minimumSwap(s1,s2))