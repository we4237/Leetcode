# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxLevel,ans = -1,0
        def dfs(node:Optional[TreeNode],level:int) -> None:
            if node is None:
                return
            nonlocal maxLevel,ans
            if level > maxLevel:
                maxLevel,ans = level,node.val
            elif level == maxLevel:
                ans += node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return ans