import collections


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        stack = collections.deque()
        for i,x in enumerate(s):
            if i < n:
                stack.append(x)
            else:
                break

        ans = s[n:]
        while stack:
            ans += stack.popleft()

        return ans

if __name__ == '__main__':
    s = "abcdefg"
    n = 2
    solution = Solution()
    print(solution.reverseLeftWords(s,n))
