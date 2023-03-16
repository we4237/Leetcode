from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for x in folder[1:]:
            m = len(ans[-1]) #已有文件路径
            n = len(x) #新文路径
            if m >= n or not ((ans[-1] == x[:m]) and x[m] == '/'):
                ans.append(x)
        return ans


folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
solution = Solution()
print(solution.removeSubfolders(folder))