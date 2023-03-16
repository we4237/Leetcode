class Solution:
    def reformat(self, s: str) -> str:
        number = []
        ABC = []

        for char in s:
            if char.isdigit():
                number.append(char)
            else:
                ABC.append(char)
        if abs(len(number)-len(ABC))>1:
            return ""
        if len(number)<len(ABC): # 长的放前面
            number,ABC = ABC,number
        ss,i,j = "",0,0
        for idx in range(len(s)):
            if idx % 2 == 0:
                ss += number[i]
                i += 1
            else:
                ss += ABC[j]
                j += 1
        return ss


s = "a0b1c2"
solution =Solution()
print(solution.reformat(s))