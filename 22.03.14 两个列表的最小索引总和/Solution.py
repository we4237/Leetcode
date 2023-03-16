from math import inf
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        index = {s:i for i,s in enumerate(list1)}
        indexSum = inf
        for i,s in enumerate(list2):
            if s in index:
                j = index[s]
                if i+j<indexSum:
                    index = i + j
                    ans = [s]
                elif i+j == indexSum:
                    ans.append(s)
        return ans

if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines","Hungry Hunter Steakhouse", "Shogun"]
    solution = Solution()
    print(solution.findRestaurant(list1,list2))
