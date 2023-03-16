class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i,c in enumerate(command):
            if c == 'G':
                res.append('G')
            elif c == '(' and command[i+1] == ')':
                res.append('o')
            elif c == '(' and command[i + 1] == 'a':
                res.append('al')
        return ''.join(res)

command = "G()(al)"
solution = Solution()
print(solution.interpret(command))