# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(num:TreeNode,res:List[int]):
            if num:
                inorder(num.left,res)
                res.append(num.val)
                inorder(num.right,res)

        num1,num2=[],[]
        inorder(root1,num1)
        inorder(root2,num2)

        merged = []
        p1, n1 = 0, len(num1)
        p2, n2 = 0, len(num2)
        while True:
            if p1 == n1:
                merged.append(num2[p2:])
                break
            if p2 == n2:
                merged.append(num1[p1:])
                break
            if num1[p1]<num2[p2]:
                merged.append(num1[p1])
                p1 += 1
            else:
                merged.append(num2[p2])
                p2 += 1
        return merged