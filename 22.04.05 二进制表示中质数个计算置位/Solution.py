class Solution:
    def isPrime(self,x:int) -> bool:
        if x<2:
            return False
        i = 2
        while i*i <=x:
            if x%i ==0 :
                return False
            i +=1
        return True

    def ccount(self, y:int) -> int:
        cnt = 0
        while (y != 0):
            y &= (y-1)
            cnt += 1
        return cnt

    def countPrimeSetBits(self, left: int, right: int) -> int:

        return sum(self.isPrime(self.ccount(x)) for x in range(left, right + 1))

if __name__ == '__main__':
    left = 6
    right = 10
    solution =Solution()
    print(solution.countPrimeSetBits(left,right))