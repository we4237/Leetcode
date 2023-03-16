class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 == 2:
                return False
            else:
                n //= 3
        return True

n = 21
solution= Solution()
print(solution.checkPowersOfThree(n))