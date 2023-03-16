
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # ne = defaultdict(int)
        # def build():
        #     ne[0],k,j = -1,0,2
        #     c = 1
        #     while True:
        #         i = j % len(word)
        #         if k != 0 and word[k % len(word)] != word[i - 1]:
        #             k = ne[k]
        #         if word[i - 1] == word[k % len(word)] :
        #             ne[j] = k + 1
        #             k += 1
        #         j += 1
        #         if j % len(word) == 0:
        #             yield c
        #             c += 1
        # m = build()
        # c = next(m)
        # j,maxl = 0,0
        # for i in range(len(sequence)):
        #     while j > 0 and word[j % len(word)] != sequence[i]:
        #         j = ne[j]
        #     if sequence[i] == word[j % len(word)]:
        #         j += 1
        #         if j % len(word) == 0:
        #             maxl = max(maxl,j // len(word))
        #             if maxl >= c :
        #                 c = next(m)
        # return maxl
        n,m = len(sequence),len(word)
        if n < m :
            return 0
        ans = [0] * n
        for i in range(m-1,n):
            valid = True
            for j in range(m):
                if sequence[i-m+1+j] != word[j]:
                    valid = False
                    j+=1
            if valid:
                ans[i] =(0  if i == m-1 else ans[i-m]) +1
        return max(ans)

sequence = "ababc"
word = "ab"
solution = Solution()
print(solution.maxRepeating(sequence,word))


