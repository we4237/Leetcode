class Solution:
    def henshin(self,perm:list) -> list:
        n = len(perm)
        ans = [0 for _ in range(n)]
        for i in range(n):
            if i % 2 == 0:
                ans[i] = perm[i//2]
            else:
                ans[i] = perm[n//2 + (i - 1)//2]
        return ans



    def reinitializePermutation(self, n: int) -> int:
        perm = [x for x in range(n)]
        count = 0
        target = perm.copy()
        while True:
            count += 1
            perm = self.henshin(perm)
            if perm == target:

                return count


n = 4
solution = Solution()
print(solution.reinitializePermutation(n))