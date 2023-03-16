class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = "!@#$%^&*()-+"
        n = len(password)
        if n < 8:
            return False
        islower = False
        isUper = False
        isdigit = False
        isspecial = False
        for i in range(n-1):
            if password[i] == password[i+1]:
                return False
        for i in range(n):
            if password[i].islower():
                islower = True
            if password[i].isupper():
                isUper = True
            if password[i].isdigit():
                isdigit = True
            if password[i] in special:
                isspecial = True
        if isspecial and islower and isUper and isdigit:
            return True
        else:
            return False


password = "1aB!"
solution = Solution()
print(solution.strongPasswordCheckerII(password))