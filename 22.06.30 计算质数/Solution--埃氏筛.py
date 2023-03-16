from math import sqrt


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         # numPrime = sum(self.isPrime(i) for i in range(1,n))
#         # return numPrime
#
#         def isPrime( n: int) -> int:
#             if n == 1:
#                 return 0
#             for i in range(2, int(sqrt(n) + 1)):
#                 if n % i == 0:
#                     return 0
#             return 1
#
#         count = 0
#         for i in range(1,n):
#             count += isPrime(i)
#         return count

class Solution:
    def countPrimes(self, n: int) -> int:
        # 定义数组标记是否是质数
        is_prime = [1] * n

        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0

        return count





n=10
solution=Solution()
print(solution.countPrimes(n))