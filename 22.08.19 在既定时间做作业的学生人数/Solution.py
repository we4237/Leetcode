from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s<= queryTime <= e for e,s in zip(endTime,startTime))