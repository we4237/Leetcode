from collections import Counter
from typing import List


class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
        #     return -1  # 优化
        # d = sum(nums2) - sum(nums1)
        # if d < 0:
        #     d = -d
        #     nums2,nums1 = nums1,nums2
        # ans = 0
        # cnt = Counter(6-x for x in nums1)+Counter(x-1 for x in nums2)

        # for i in range(5,0,-1):
        #     if i * cnt[i] >= d:
        #         return ans+(d+i-1)//i
        #     ans += cnt[i]
        #     # i个cnt[i]也不能使d等于0
        #     d -= i*cnt[i]

        # sum2 > sum1
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1>s2:
            return self.minOperations(nums2,nums1)
        elif s1 == s2:
            return 0
        ans,diff,cnt,i =0 ,s2-s1, Counter(nums1+[7-num for num in nums2]),1
        while diff and i<=5:
            for _ in range(cnt[i]):
                if not diff:
                    break
                if diff >= 6-i:
                    diff -= 6-i
                else:
                    diff = 0
                ans +=1
            i += 1
        return -1 if diff>0 else ans




nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]
solution = Solution()
print(solution.minOperations(nums1,nums2))