from collections import Counter, defaultdict


class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        cnt = []
        i,j = 0,0
        while i < n and j < n:
            if S[i] == S[j]:
                j += 1
                if j == n:
                    cnt.append(S[i])
                    cnt.append(str(j - i))
            else:
                cnt.append(S[i])
                cnt.append(str(j-i))
                i = j

        return ''.join(cnt) if len(cnt) < len(S) else S

S = "aabcccccaaa"
solution = Solution()
print(solution.compressString(S))
