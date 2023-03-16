class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def dfs(node:'Node'):
            if node is None:
                return
            ans.append(node.val)
            for ch in node.children:
                dfs(ch)
        dfs(root)
        return ans



#if __name__ =='__main__':

