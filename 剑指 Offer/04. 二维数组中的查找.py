from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        n,m = len(matrix),len(matrix[0])
        i,j = 0,n-1
        while i < m and j >= 0:
            if matrix[j][i] < target:
                i += 1
            elif matrix[j][i] > target:
                j -= 1
            else:
                return True

        return False

# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
matrix = [[1,1]]
solution = Solution()
print(
    solution.findNumberIn2DArray(matrix,target=2)
)
