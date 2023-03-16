from typing import List


class Node:
    def __init__(self):
        self.minVal = 1e4
        self.maxVal = 0
        self.minStr = ""
        self.maxStr = ""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        dp = [[Node()for _ in range(n)] for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i].minVal = num
            dp[i][i].maxVal = num
            dp[i][i].minStr = str(num)
            dp[i][i].maxStr = str(num)
        for i in range(n):
            for j in range(n-i):
                for k in range(j, j+i):
                    # 最大值
                    if dp[j][j + i].maxVal < dp[j][k].maxVal / dp[k + 1][j + i].minVal:
                        dp[j][j + i].maxVal = dp[j][k].maxVal / dp[k + 1][j + i].minVal
                        if k + 1 == j + i:
                            dp[j][j + i].maxStr = dp[j][k].maxStr + "/" + dp[k + 1][j + i].minStr
                        else:
                            dp[j][j + i].maxStr = dp[j][k].maxStr + "/(" + dp[k + 1][j + i].minStr + ")"


                    # 最小值
                    if dp[j][j + i].minVal > dp[j][k].minVal / dp[k + 1][j + i].maxVal:
                        dp[j][j + i].minVal = dp[j][k].minVal / dp[k + 1][j + i].maxVal
                        if k + 1 == j + i:
                            dp[j][j + i].minStr = dp[j][k].minStr + "/" + dp[k + 1][j + i].maxStr
                        else:
                            dp[j][j + i].minStr = dp[j][k].minStr + "/(" + dp[k + 1][j + i].maxStr + ")"
        return dp[0][n - 1].maxStr




class Main:
    list = [1000, 100, 10, 2]
    solution = Solution()
    str = solution.optimalDivision(list)
    print(str)



