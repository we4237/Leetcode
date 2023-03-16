# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node:Optional[TreeNode]) -> str: #序列化
            if not node:
                return ""

            serial = "".join([str(node.val),"(",dfs(node.left),")(",dfs(node.right),")"])
            if (tree := seen.get(serial,None)): # 哈希映射
                repeat.add(tree)
            else:
                seen[serial] = node
            return serial

        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)