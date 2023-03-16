from collections import defaultdict
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dict = defaultdict(int)
        ans = []
        for name in names:
            if name not in dict.keys():
                ans.append(name)
                dict[name] = 1

            else:
                k = dict[name]
                while name+'('+str(k)+')' in dict.keys():
                    k += 1

                t = name+'('+str(k)+')'
                ans.append(t)
                dict[t] += 1
                # 更新原始名称,方便调用
                dict[name] = k+1
        return ans

names = ["gta","gta(1)","gta","avalon"]
# names = ["wano","wano","wano","wano"]
solution = Solution()
print(
    solution.getFolderNames(names)
)