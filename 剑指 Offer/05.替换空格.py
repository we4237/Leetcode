class Solution:
    def replaceSpace(self, s: str) -> str:
        n = len(s)
        str1 = ''
        for i in s:
            if i == ' ':
                str1 = str1 + '%20'
            else:
                str1 = str1 + i
        return str1

if __name__ == '__main__':
    s = "We are happy."
    solution = Solution()
    print(solution.replaceSpace(s))
