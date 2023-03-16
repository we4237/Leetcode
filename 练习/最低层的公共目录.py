from collections import defaultdict


class Tree:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def lujing(self,i:str,j:str)->str:
        way = "a(b(e,f(g,h)),c,d(i,j))"
        way = way.replace(',','') # way = "a(b(ef(gh))cd(ij))"

        haxi = defaultdict()
        tree = []
        stack = []
        for c in way:
            if c != ')':
                stack.append(c)
            elif c == ')':
                tmp = []
                # 注意stack不为空才可以读取栈顶
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop()
                    for x in tmp:
                        haxi[x] = stack[-1]

        l1,l2 = i,j
        while l1 != l2:
            l1 = haxi.get(l1,j)
            l2 = haxi.get(l2,i)
        return l1

x = 'f'
y = 'g'
solution = Solution()
print(solution.lujing(x,y))