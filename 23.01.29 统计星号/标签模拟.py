class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        n = len(s)
        valid = True
        for c in s:
            if c == '|':
                valid = not valid
            elif c == '*' and valid:
                res += 1

        return res

s = "l|*e*et|c**o|*de|"
solution = Solution()
print(solution.countAsterisks(s))
