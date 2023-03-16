from typing import List




class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x,y = 1,1000
        while x <= 1000 and y > 0:
            res = customfunction.f(x,y)
            if res > z:
                y -= 1
            elif res < z:
                x += 1
            else:
                ans.append([x,y])
                x += 1
                y -= 1
        return ans