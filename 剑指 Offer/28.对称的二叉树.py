# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(A,B):
            if A is None and B is None:return True
            if A is None or B is None:return False
            if A.val != B.val:return False
            return isMirror(A.left,B.right) and isMirror(A.right,B.left)

        return isMirror(root.left, root.right) if root else True
