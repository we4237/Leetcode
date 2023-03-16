class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        fir ,sec = len(first),len(second)
        if abs(fir-sec)>1:
            return False
        if fir == sec:
            return sum(i != j for i,j in zip(first,second)) <= 1
        else:
            if fir > sec:
                fir ,sec = sec,fir
                first,second=second,first
            i,j = 0,0
            cnt = 0
            while i<fir and j <sec:
                if first[i] != second[j]:
                    j += 1
                    cnt += 1
                else :
                    i+=1
                    j+=1
            return cnt <=1

first = "pales"
second = "pal"
solution = Solution()
print(solution.oneEditAway(first,second))