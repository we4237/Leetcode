class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,ans = -1,0
        cnt = set()
        for i in range(n):
            if i != 0:
                cnt.remove(s[i-1])
            while l + 1 < n and s[l+1] not in cnt:
                cnt.add(s[l+1])
                l += 1
            ans = max(ans,l-i+1)
        return ans

