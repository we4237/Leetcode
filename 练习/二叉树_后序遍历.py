from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder :
            return True
        root = postorder[-1]
        n = len(postorder)
        left = 0
        while left<n and postorder[left]<root:
            left += 1
        for j in range(left,n-1):
            if postorder[j]<=root:
                return False
        return self.verifyPostorder(postorder[:left]) and self.verifyPostorder(postorder[left:-1])