from collections import Counter
from string import ascii_lowercase
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0
        left = Counter(letters)
        score = dict(zip(ascii_lowercase, score))  # 字母对应的分数

        def dfs(i:int,total:int) -> None:
            if i < 0:
                nonlocal ans
                ans = max(ans,total)
                return

            # 不选words[i]
            dfs(i-1,total)

            # 选words[i]
            for j,c in enumerate(words[i]):
                if left[c] == 0:
                    # 该单词里的每一个都回溯
                    for c in words[i][:j]:

                        left[c] += 1
                    return
                left[c] -= 1
                total += score[c]

            dfs(i-1,total)

            # 回溯,恢复现场,使left中字符数量与words保持一致
            for c in words[i]:
                left[c] += 1

        dfs(len(words)-1,0)


        return ans


words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
solution = Solution()
print(
    solution.maxScoreWords(words,letters,score)
)

