# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parent = {root:None}

        # def dfs(root):
        #     if root:
        #         if root.left:
        #             parent[root.left] = root
        #         if root.right:
        #             parent[root.right] = root
        #         dfs(root.left)
        #         dfs(root.right)

        def dfs(root):
            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)

        dfs(root)

        l1 , l2 = p,q
        while(l1!=l2):
            l1 = parent.get(l1,q)
            l2 = parent.get(l2,p)

        return l1


a = TreeNode(2)
a.left = TreeNode(7)
a.right = TreeNode(4)
b = TreeNode(5)
b.left = TreeNode(6)
b.right = a
c = TreeNode(1)
c.left = TreeNode(0)
c.right = TreeNode(8)
root = TreeNode(3)
root.left = b
root.right = c
p = TreeNode(5)
q = TreeNode(1)

solution = Solution()
print(solution.lowestCommonAncestor(root,p,q))