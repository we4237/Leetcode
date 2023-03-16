from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        best,ans=float('inf'),list()
        for i in range(n-1):
            if (data := arr[i+1]-arr[i]) < best:
                best = data
                ans = [[arr[i], arr[i + 1]]]
            elif data == best:
                ans.append([arr[i],arr[i+1]])
        return ans

arr = [40,11,26,27,-20]
solution = Solution()
print(solution.minimumAbsDifference(arr))