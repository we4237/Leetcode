class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) >= len(sentence2):
            long = sentence1
            short = sentence2
        else:
            long = sentence2
            short = sentence1
        shortlist = short.split(' ')
        longlist = long.split(' ')
        m = len(longlist)
        n = len(shortlist)
        i = j = 0
        while i < n and longlist[i] == shortlist[i]:
            i += 1
        while j < n and longlist[m-1-j] == shortlist[n-1-j]:
            j += 1

        return i + j >= n

sentence1 = "CwFfRo regR"
sentence2 = "CwFfRo H regR"
solution = Solution()
print(solution.areSentencesSimilar(sentence1,sentence2))