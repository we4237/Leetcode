import math
from collections import Counter
#
# 现在给你一个包含 n 个正整数的序列a，你可以进行许多次操作直到序列为空，每次操作可以选定当前序列中的一个数ai并删除，然后删除所有等于ai+1或者ai-1的数，删除的数无法再被之后的操作选中，这样的一次操作能让你获得ai分，请问你最多能获得多少分数。

len = 5
numbers = [1,2,3,2,2]

res = 0
cnt = Counter(numbers)
Max = 0
Min = math.inf

while not all(x == 0 for x in cnt.values()):
    most = cnt.most_common()
    Max = most[0][1]
    Maxnumber = most[0][0]
    Min = most[-1][1]
    Minnumber = most[-1][0]

    res += (Max - Min)*Maxnumber
    a = cnt[Minnumber] if cnt[Minnumber] else 1
    cnt[Maxnumber] = cnt[Maxnumber] - (Max - Min)*a if cnt[Maxnumber] - (Max - Min)*cnt[Minnumber] > 0  else 0
    cnt[Maxnumber-1] = cnt[Maxnumber-1] - (Max - Min)*a if cnt[Maxnumber-1] - (Max - Min)*cnt[Minnumber]> 0  else 0
    cnt[Maxnumber+1] = cnt[Maxnumber+1] - (Max - Min)*a if cnt[Maxnumber+1] - (Max - Min)*cnt[Minnumber]> 0  else 0

print(res)
