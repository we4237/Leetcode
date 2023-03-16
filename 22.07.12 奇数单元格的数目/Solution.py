from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for x,y in indices:
            for j in range(n):
                matrix[x][j] += 1
            for row in matrix:
                row[y] += 1
        return sum(x % 2 for row in matrix for x in row)