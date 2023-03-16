# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        curNode = root
        nextNode = None
        stack = deque()
        while curNode != p:
            stack.append(curNode)
            if p.val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right

        # curNode has subtree, search down
        if curNode.right:
            nextNode = curNode.right
            while nextNode.left:
                nextNode = nextNode.left
            return nextNode

        # curNode does not have subtree, search up
        if len(stack) > 0:
            preNode = stack.pop()
            while preNode:
                if p.val > preNode.val:
                    if len(stack) > 0:
                        preNode = stack.pop()
                    else:
                        return None
                else:
                    return preNode

