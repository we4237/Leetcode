s = [1,2,2]
i = 2
one = True
while len(s)<= 100000:
    s += [1 if one else 2] * s[i]
    one = not one
    i += 1
cnt = [0] * (len(s) + 1)
for i in range(len(s)):
    cnt[i+1] += cnt[i] + (s[i] == 1)



class Solution:
    def magicalString(self, n: int) -> int:
        # return cnt[n]
        s = [1,2,2]
        i = 2
        while(len(s)<n):
            s += [3-(s[-1])] * s[i]
            i += 1
        return s[:n].count(1)