class Solution:
    def minimumMoves(self, s: str) -> int:
        coverd = -1
        res = 0
        for i,c in enumerate(s):
            if c == 'X' and i > coverd: # cover相当于跳三个
                res += 1
                coverd = i + 2
        return res

s = "OXOX"
solution = Solution()
print(solution.minimumMoves(s))