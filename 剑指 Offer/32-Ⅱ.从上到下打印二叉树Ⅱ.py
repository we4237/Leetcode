# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:return []
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            tmp = []

            for _ in range(len(queue)):

                node = queue.popleft()
                tmp.append(node.val)
                if node.left :queue.append(node.left)
                if node.right:queue.append(node.right)
            ans.append(tmp)
        return ans