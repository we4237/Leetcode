from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s.replace('(','').replace(')','')
        n = len(s)
        def if_valid(sn)-> List[str]:
            valid = []
            for i in range(1,len(sn)+1):
                if len(sn) == 1 and sn[:i] == '0':
                    valid.append(sn[:i])
                    continue
                if i == len(sn) and sn[0] != '0':
                    valid.append(sn[:i])
                    continue


                s_zheng = sn[:i]
                if s_zheng[0] == '0' and len(s_zheng) > 1:
                    continue

                s_xiao = sn[i:]
                if s_xiao[len(s_xiao)-1] == '0':
                    continue

                valid.append(s_zheng+'.'+s_xiao)

            return valid


        res = []
        X = []
        Y = []
        for i in range(1,n):
            s1 = s[:i]
            s2 = s[i:]
            x = if_valid(s1)
            X.append(x)
            y = if_valid(s2)
            Y.append(y)

        for i in range(n - 1):

            for x in X[i]:
                for y in Y[i]:
                    res.append(f'({x}, {y})')

        return res




s = "(00011)"
solution = Solution()
print(solution.ambiguousCoordinates(s))
