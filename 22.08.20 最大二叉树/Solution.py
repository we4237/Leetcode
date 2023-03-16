# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

# dfs
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         def dfs(left,right):
#             if left<right:
#                 v,index = nums[left],left
#                 for i in range(left+1,right):
#                     if nums[i] > v:
#                         index ,v = i, nums[i]
#                 return TreeNode(v,dfs(left,index),dfs(index+1,right))
#         return dfs(0 , len(nums))


# 单调栈
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stk = list()
        left,right = [-1]*n,[-1]*n
        tree = [None]*n

        for i in range(n):
            tree[i]=TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i]=stk[-1]
            stk.append(i)

        root = None
        for i in range(n):
            if left[i] == right[i] == -1:
                root = tree[i]
            elif right[i] == -1 or (left[i] != -1 and nums[left[i]]<nums[right[i]]):
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]

        return root

nums = [3,2,1,6,0,5]
solution = Solution()
solution.constructMaximumBinaryTree(nums)