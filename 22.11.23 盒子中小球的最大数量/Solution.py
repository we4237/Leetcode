

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        haxi = [0 for _ in range(10000)]
        def calculate(x:int)->int:
            count = 0
            sum = 0
            long = len(str(x))
            while count < long:
                sum += x % 10
                x = x // 10
                count += 1
            return sum

        for item in range(lowLimit,highLimit+1):
            haxi[calculate(item)] += 1



        return max(haxi)

lowLimit = 1
highLimit = 10
solution = Solution()
print(solution.countBalls(lowLimit,highLimit))