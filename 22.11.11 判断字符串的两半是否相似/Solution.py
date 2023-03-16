class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s = list(s)
        s1 = s[:n//2]
        s2 = s[n//2:]

        up = ['A','E','I','O','U']
        low =['a','e','i','o','u']

        ans_s1 = []
        ans_s2 = []

        for c in s1:
            if c.isupper() and c in up:
                ans_s1.append(c)
            elif c.islower() and c in low:
                ans_s1.append(c)
        for b in s2:
            if b.isupper() and b in up:
                ans_s2.append(b)
            elif b.islower() and b in low:
                ans_s2.append(b)

        # ans_s1 = ''.join(sorted(ans_s1))
        # ans_s2 = ''.join(sorted(ans_s2))
        if len(ans_s1) == len(ans_s2):
            return True
        else:
            return False




s = "AbCdEfGh"
solution = Solution()
print(solution.halvesAreAlike(s))