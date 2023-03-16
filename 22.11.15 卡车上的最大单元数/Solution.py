from typing import List

import numpy as np


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        size = truckSize
        box = sorted(boxTypes,key = lambda x:x[1],reverse=True)
        box_size = [box[n][1] for n in range(len(box))]
        box_number = [box[n][0] for n in range(len(box))]
        sum = 0

        for i,x in zip(box_number,box_size):
            if i >= size:
                sum += size * x
                size = 0
            else:
                sum += i * x
                size -= i
            if size == 0:
                break
        return sum





boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize =   35
solution = Solution()
print(solution.maximumUnits(boxTypes,truckSize))
