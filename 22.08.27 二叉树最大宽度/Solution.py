# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         res = 1
#         arr = [[root,1]]
#         while arr:
#             tmp = []
#             for node,index in arr:
#                 if node.left:
#                     tmp.append([node.left,index*2])
#                 if node.right:
#                     tmp.append([node.right,index*2+1])
#
#             res = max(res,arr[-1][1]-arr[0][1]+1)
#             arr = tmp
#         return res

# DFS
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelMin = {}
        def dfs(node:Optional[TreeNode],depth:int,index:int) -> int:
            if node is None:
                return 0
            if depth not in levelMin:
                levelMin[depth] = index # 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return max(index - levelMin[depth] + 1,
                       dfs(node.left,depth+1,index*2),
                       dfs(node.right,depth+1,index*2+1))
        return dfs(root,1,1)