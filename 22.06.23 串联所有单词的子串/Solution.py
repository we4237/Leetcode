from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res =[]
        words_num,word_len,s_len = len(words),len(words[0]),len(s)
        for i in range(word_len):
            if i + words_num*word_len >s_len:
                break

            differ = Counter()
            for j in range(words_num):
                word = s[i+j*word_len:i+(j+1)*word_len]
                differ[word]+=1

            for word in words:
                differ[word]-=1
                if differ[word]==0:
                    del differ[word]

            for start in range(i,s_len-words_num*word_len+1,word_len):
                if start != i:
                    word = s[start + (words_num-1)*word_len : start + words_num*word_len]
                    differ[word]+=1
                    if differ[word]==0:
                        del differ[word]
                    word=s[start-word_len:start]
                    differ[word]-=1
                    if differ[word]==0:
                        del differ[word]
                if len(differ)==0:
                    res.append(start)
        return res

s = "barfoothefoobarman"
words = ["foo","bar"]
solution=Solution()
print(solution.findSubstring(s,words))