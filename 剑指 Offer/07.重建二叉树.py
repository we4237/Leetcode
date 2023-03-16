# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def rebuildTree(preorderID,inleft,inright):
            if inleft > inright:return
            rootval = preorder[preorderID]
            inorder_rootID = index[rootval]
            leftsize = inorder_rootID - inleft
            # 创建二叉树
            node = TreeNode(rootval)
            node.left = rebuildTree(preorderID+1,inleft,inorder_rootID-1)
            node.right = rebuildTree(preorderID+1+leftsize,inorder_rootID+1,inright)
            return node

        index = {val:i for i,val in enumerate(inorder)}
        return rebuildTree(0,0,len(inorder)-1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
print(solution.buildTree(preorder,inorder))