class Solution:
    def minimumDeletions(self, s: str) -> int:
        a,b = 0,0
        n = len(s)
        for i in range(n):
            if s[i] == 'a':
                a += 1
            else:
                b = max(a,b)+1
        return n - max(a,b)

s = "aababbab"
solution = Solution()
print(solution.minimumDeletions(s))