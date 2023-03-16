from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        window,dict = [] ,{}
        for num in nums2:
            while window and num > window[-1]:
                small = window.pop() # 单调栈
                dict[small] = num
            window.append(num)
        return [dict[num] if num in dict.keys() else -1 for num in nums1 ]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
solution = Solution()
print(solution.nextGreaterElement(nums1, nums2))
