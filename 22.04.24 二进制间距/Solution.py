class Solution:
    def binaryGap(self, n: int) -> int:
        last,ans,i = -1,0,0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans,i - last)
                last = i
            n >>= 1
            i += 1

        return ans

n = 22
solution = Solution()
print(solution.binaryGap(n))