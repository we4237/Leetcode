from typing import List


# class WordFilter:
#
#     def __init__(self, words: List[str]):
#         self.dic = {} # 哈希表
#         for idx,word in enumerate(words):
#             m = len(word)
#             for prefixLength in range(1,m+1):
#                 for suffixLength in range(1,m+1):
#                     self.dic[word[:prefixLength]+'#'+word[-suffixLength:]] = idx
#
#     def f(self, pref: str, suff: str) -> int:
#         return self.dic.get(pref+'#'+suff,-1)

# 字典树
class TreeNode:
    def __init__(self,ch):
        self.ch = ch
        self.is_end = False
        self.children = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        idx_dict = {}
        for word in words: # 找到每一个单词的最后索引
            idx = len(words)-1-words[::-1].index(word)
            idx_dict[word]=idx
        self.root = TreeNode("")
        for word in words:
            res = self.transform(word)
            for r in res:
               node = self.root
               for ch in r:
                   if ch not in node.children:
                       node.children[ch]=TreeNode(ch)
                   node = node.children[ch]
               node.is_end = True
               node.index = idx_dict[word]

    @staticmethod
    def transform(word):
        res = []
        for i in range(len(word)):
            suf = word[i:]
            new_w = suf + "#" +word
            res.append(new_w)
        return res

    def search(self,node,res):
        if node.is_end:
            res.append(node.index)
        for _,n in node.children.items():
            self.search(n,res)


    def f(self, pref: str, suff: str) -> int:
        new_w = suff+"#"+pref
        node = self.root
        valid=[]
        for ch in new_w:
            if ch not in node.children:
                return -1
            node = node.children[ch]
        res = []
        self.search(node,res)
        return max(res)


if __name__ =="__main__":
    # Your WordFilter object will be instantiated and called as such:
    words = ["apple"]
    pref = "a"
    suff = "e"
    obj = WordFilter(words)
    param_1 = obj.f(pref,suff)
    print(param_1)