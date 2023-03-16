from math import sqrt


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        numPrime = sum(self.isPrime(i) for i in range(1,n+1))
        return self.factorial(numPrime)*self.factorial(n-numPrime)%(10**9 +7)

    def isPrime(self,n:int)->int:
        if n==1:
            return 0
        for i in range(2,int(sqrt(n)+1)):
            if n % i ==0:
                return 0
        return 1

    def factorial(self,n:int)->int:
        res = 1
        for i in range(1,n+1):
            res *= i
            res %= (10**9 +7)
        return res


n = 100
solution=Solution()
print(solution.numPrimeArrangements(n))