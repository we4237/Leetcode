from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0]*n
        for left,right,inc in bookings:
            nums[left-1] += inc
            if right<n:
                nums[right] -= inc
        for i in range(1,n):
            nums[i] += nums[i-1]

        return nums

if __name__ =='__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    solution = Solution()
    print(solution.corpFlightBookings(bookings,n))

