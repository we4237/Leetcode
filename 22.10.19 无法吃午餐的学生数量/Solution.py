from collections import Counter
from typing import List


# class Solution:
    # def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    #     cnt = Counter(students)
    #     for i,sandwiche in enumerate(sandwiches):
    #         if cnt[sandwiche] == 0:
    #             return len(sandwiches)-i
    #         cnt[sandwiche] -= 1
    #     return 0

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sand0,sand1 = 0,0
        for stu in students:
            if stu == 1:
                sand1 += 1
            else:
                sand0 += 1
        for i,san in enumerate(sandwiches):
            if san == 1:
                sand1 -= 1
            else:
                sand0 -= 1
            if sand1 < 0 or sand0 < 0:
                return len(sandwiches)-i
        return sand0 + sand1

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
solution = Solution()
print(solution.countStudents(students,sandwiches))