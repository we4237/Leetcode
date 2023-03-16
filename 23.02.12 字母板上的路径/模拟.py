from collections import defaultdict

board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

# 笨方法
# class Solution:
#     def alphabetBoardPath(self, target: str) -> str:
#         ans = []
#         n = len(board)
#         haxi = defaultdict(list)
#         start = 'a'
#         for row in range(n):
#             for line in range(len(board[row])):
#                 alpha = board[row][line]
#                 haxi[alpha] = [row,line]
#         for i in target:
#             dist_y = haxi[i][0] - haxi[start][0]
#             dist_x = haxi[i][1] - haxi[start][1]
#             start = i
#             if dist_x == 0 and dist_y == 0:
#                 ans.append('!')
#                 continue
#             elif dist_x <= 0 and dist_y <= 0:
#                 ans.append('U'*abs(dist_y))
#                 ans.append('L'*abs(dist_x))
#                 ans.append('!')
#
#             elif dist_x >= 0 and dist_y <= 0:
#                 ans.append('U'*abs(dist_y))
#                 ans.append('R'*abs(dist_x))
#
#                 ans.append('!')
#             elif dist_x <= 0 and dist_y >= 0:
#
#                 ans.append('D'*abs(dist_y))
#                 ans.append('L'*abs(dist_x))
#
#                 ans.append('!')
#             else:
#                 ans.append('D'*abs(dist_y))
#                 ans.append('R'*abs(dist_x))
#
#                 ans.append('!')
#         return ''.join(ans)

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        x = y = 0
        pre = 'a'
        res = []
        for c in target:
            if c == pre:
                res.append('!')
                continue
            c = ord(c) - ord('a') # 不浪费内存
            nx = c // 5
            ny = c % 5
            if nx < x:
                res.append('U' * (x - nx))
            if ny < y:
                res.append('L' * (y - ny))

            if nx > x:
                res.append('D' * (nx - x))
            if ny > y :
                res.append('R' * (ny - y))

            res.append('!')
            x = nx
            y = ny
            pre = c
        return ''.join(res)


target = "zdz"
solution = Solution()
print(solution.alphabetBoardPath(target))

