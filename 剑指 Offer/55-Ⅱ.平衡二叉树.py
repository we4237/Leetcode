# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(root) -> int:
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            return max(max_right, max_left) + 1
        return abs(dfs(root.left)-dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
