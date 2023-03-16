from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # ans = 0
        # for item in items:
        #
        #         if ruleKey == "type" and item[0] == ruleValue:
        #                 ans += 1
        #         elif ruleKey == "color" and item[1] == ruleValue:
        #                 ans += 1
        #         elif ruleKey == "name" and item[2] == ruleValue:
        #                 ans += 1
        # return ans



        index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[index] == ruleValue for item in items)


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
solution = Solution()
print(solution.countMatches(items,ruleKey,ruleValue))
