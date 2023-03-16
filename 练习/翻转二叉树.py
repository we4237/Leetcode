# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class BinaryTree(object):  # 创建二叉树
#     def __init__(self):
#         self.root = None  #根节点
#
#     def add(self, val):  # 二叉树添加结点
#         node = TreeNode(val)
#         if self.root is None:
#             self.root = node
#             return
#         queue = [self.root]
#         while queue:
#             temp_node = queue.pop(0)
#             if temp_node.left is None:
#                 temp_node.left = node
#                 return
#             else:
#                 queue.append(temp_node.left)
#             if temp_node.right is None:
#                 temp_node.right = node
#                 return
#             else:
#                 queue.append(temp_node.right)
#
#     def bre_order(self,node):  # 二叉树的广度遍历
#         if node is None:
#             return
#         queue = [node]
#         while queue:
#             temp_node = queue.pop(0)
#             print(temp_node.val,end=" ")
#             if temp_node.left is not None:
#                 queue.append(temp_node.left)
#             if temp_node.right is not None:
#                 queue.append(temp_node.right)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class Main:
    B = TreeNode(1,None,None)
    C = TreeNode(3,None,None)

    root = TreeNode(2, B, C)



    solution = Solution()
    print(solution.invertTree(root))

