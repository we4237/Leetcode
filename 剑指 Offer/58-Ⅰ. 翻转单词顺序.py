class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split(' ')
        stack = []
        for x in tmp:
            if x != '':
                stack.append(x)

        ans = []
        while stack:
            ans.append(stack.pop())
        return ' '.join(ans)

s = "  hello world!  "
solution = Solution()
print(solution.reverseWords(s))