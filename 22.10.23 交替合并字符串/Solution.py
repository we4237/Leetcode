# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         ans = []
#         n,m = len(word1),len(word2)
#         i,j = 0,0
#         while i < n or j < m:
#             if i < n :
#                 ans.append(word1[i])
#                 i += 1
#             if j < m:
#                 ans.append(word2[j])
#                 j += 1
#         return ('').join(ans)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m,i,j = len(word1),len(word2),0,0
        ans = ""
        while i < n or j < m:
            if i < n:
                ans += word1[i]
                i += 1
            if j < m :
                ans += word2[j]
                j += 1
        return ans

word1 = "ab"
word2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word1,word2))
