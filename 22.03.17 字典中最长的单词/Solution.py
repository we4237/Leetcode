from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key=len,reverse = True)
        words_set = set(words)

        for w in words:
            flag = False
            for i in range(1,len(w)+1):
                if w[:i] not in words_set:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True:
                return w
        return ''

if __name__ =="__main__":
    words = ["w", "wo", "wor", "worl", "world"]
    solution = Solution()
    print(solution.longestWord(words))