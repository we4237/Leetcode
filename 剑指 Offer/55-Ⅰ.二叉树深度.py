# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:  return 0
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return max(max_right,max_left)+1