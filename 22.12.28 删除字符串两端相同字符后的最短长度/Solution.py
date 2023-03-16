class Solution:
    def minimumLength(self, s: str) -> int:
        left,right = 0 , len(s) - 1
        while left<right and s[left]==s[right]:
            while left + 1 < right and s[left]==s[left+1]:
                left += 1
            while left < right - 1 and s[right-1]==s[right]:
                right -= 1
            left,right = left + 1, right - 1
        return max(0,right-left+1)