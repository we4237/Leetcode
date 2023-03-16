# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from collections import deque


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
#        """
# class Solution:
#     def deserialize(self, s: str) -> NestedInteger:
#         stack = deque()
#         num = ""
#         for c in s:
#             if c =="[":
#                 # 添加结构体
#                 stack.append(NestedInteger())
#             elif c in [',',']']:
#                 if len(num)>1: # num不为空
#                     stack[-1].add(NestedInteger(int(num)))
#                     num = ""
#                 if c==']' and len(stack)>1:
#                     stack[-2].add(stack.pop())
#             else:
#                 # c is 0-9 or -
#                 num += c
#         return stack[0] if len(stack) > 0 else NestedInteger(int(num))

from collections import deque
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = deque()
        num = ""
        for c in s:
            if c=='[':
                stack. append (NestedInteger())
            elif c in [',', ']']:
                if len(num) > 0:
                    # NOTE， int() in python handles negative numbers
                    stack[-1] . add(NestedInteger(int(num)))
                    num = ""
                if c ==']' and len(stack) > 1:
                    stack [-2] .add(stack.pop())
            else:
                # cis0-9or-
                num += c
        return stack[0] if len(stack) > 0 else NestedInteger( int(num) )

