from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        j = 0
        while j < n:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        i -= 1
        j -= 1
        while i >= 0:
            if j < n :
                arr[j] = arr[i]
            if arr[i] == 0 and j-1 >= 0:
                j = j - 1
                arr[j] = 0
            i-=1
            j-=1


arr = [1,0,2,3,0,4,5,0]
solution = Solution()
solution.duplicateZeros(arr)
print(arr)