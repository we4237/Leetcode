# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def callDepth(node:Optional[TreeNode]):
            return max(callDepth(node.left)+1 if node.left else 0,callDepth(node.right)+1 if node.right else 0)
        height = callDepth(root)

        m = height + 1
        n = 2**m -1
        ans = [['']*n for _ in range(m)]
        def dfs(node:Optional[TreeNode],r:int,center:int):
            ans[r][center]=str(node.val)
            if node.left:
                dfs(node.left,r+1,center-2**(height-r-1))
            if node.right:
                dfs(node.right, r + 1, center + 2 ** (height - r - 1))
        dfs(root,0,(n-1)//2)

        return ans