class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1
        while n != 0:
            y = x + y
            x = y - x
            n -= 1
        return x % 1000000007

n = 2
solution = Solution()
print(
    solution.fib(n)
)