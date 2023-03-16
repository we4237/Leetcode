from collections import defaultdict
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.flag = -1

    def insert(self,i,f):
        node = self
        ps = f.split('/')
        for x in ps[1:]:
            if x not in node.children:
                node.children[x] = Trie()
            node = node.children[x]
        node.flag = i

    def search(self):

        def dfs(root):
            if root.flag != -1:
                ans.append(root.flag)
                return
            for child in root.children.values():
                dfs(child)

        ans = []
        dfs(self)
        return ans

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        tree = Trie()
        for i, f in enumerate(folders):
            tree.insert(i,f)
        return [folders[i] for i in tree.search()]

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
solution = Solution()
print(solution.removeSubfolders(folder))
