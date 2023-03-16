from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        nameandTime = defaultdict(list)
        for name,time in zip(keyName,keyTime):
            hour,minute = int(time[:2]),int(time[3:])
            nameandTime[name].append(hour*60+minute)

        ans = []
        for name,times in nameandTime.items():
            times.sort()
            if any(t2 - t1 <= 60 for t1,t2 in zip(times,times[2:])):
                ans.append(name)


        ans.sort()

        return ans

keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]

solution = Solution()
print(solution.alertNames(keyName,keyTime))
