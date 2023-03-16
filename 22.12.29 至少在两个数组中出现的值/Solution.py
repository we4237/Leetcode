from collections import defaultdict
from typing import List

# 位运算+哈希
# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         dict = defaultdict(int)
#         for i,nums in enumerate((nums1,nums2,nums3)):
#             for x in nums:
#                 dict[x] |= 1<<i
#         return [x for x,m in dict.items() if m & (m-1)]

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return [i for i in range(1, 101) if (i in s1) + (i in s2) + (i in s3) > 1]

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
solution = Solution()
print(solution.twoOutOfThree(nums1,nums2,nums3))

