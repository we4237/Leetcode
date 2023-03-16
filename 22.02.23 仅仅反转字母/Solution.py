class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left,right = 0, len(ans)-1
        while True:
            while left < right and not ans[left].isalpha():
                left += 1
            while right > left and not ans[right].isalpha():
                right -=1
            if left >= right:
                break
            #交换
            ans[left],ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)

class Main:
    s = 'ab-cd'
    solution = Solution()
    print(solution.reverseOnlyLetters(s))


