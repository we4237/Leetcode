class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        n = len(word)
        left = 0
        while True:
            while left < n and word[left].isalpha():
                left += 1
            if left == n:
                break
            right = left
            while right < n and word[right].isdigit():
                right += 1
            while right - left > 1 and word[left]=='0':
                left += 1
            s.add(word[left:right])
            left = right
        return len(s)



word = "a123bc34d8ef34"
solution = Solution()
print(solution.numDifferentIntegers(word))
