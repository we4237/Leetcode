class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        def kmp(T:str,p:str) -> int:
            n,m = len(T),len(p)

            next = generateNext(p)

            i,j = 0,0
            while i<n and j<m:
                if j == -1 or T[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if j == m:
                return i-j

            return -1


        def generateNext(p:str):
            m = len(p)
            next = [-1 for _ in range(m)]
            i,j = 0,-1
            while i < m-1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    if p[i] == p[j]:
                        next[i] = next[j]
                    else:
                        next[i] = j
                else:
                    j = next[j]
            return next


        if needle not in haystack:
            return -1
        else:
            return kmp(haystack,needle)


haystack = "hello"
needle = "ll"
solution = Solution()
print(solution.strStr(haystack,needle))