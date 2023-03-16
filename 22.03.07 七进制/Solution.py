class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = num<0
        if num == 0:
            return "0"
        number = []
        num = abs(num)
        while num:
            number.append(str(num%7))
            num //= 7
        if negative:
            number.append('-')
        return ''.join(reversed(number))

if __name__ == '__main__':
    num = -7
    solution = Solution()
    print(solution.convertToBase7(num))