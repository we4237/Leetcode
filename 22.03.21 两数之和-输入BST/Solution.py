# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set() # 哈希表
        q = deque([root]) # 队列
        while q:
            node = q.popleft()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        # 深度优先搜索 + 中序遍历
        def inorderTraversal(node:Optional[TreeNode]) -> None:
            if node:
                inorderTraversal(node.left)
                arr.append(node.val)
                inorderTraversal(node.right)
        inorderTraversal(root)

        left,right = 0,len(arr)-1
        while left < right:
            sum = arr[left] + arr[right]
            if sum == k:
                return True
            if sum<k:
                left +=1
            if sum>k:
                right +=1
        return  False





