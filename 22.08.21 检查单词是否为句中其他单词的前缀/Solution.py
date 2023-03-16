class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i,index,n = 0,1,len(sentence)
        while i < n:
            start = i
            while i < n and sentence[i] != ' ':
                i += 1
            end = i
            if sentence[start:end].startswith(searchWord):
                return index
            index += 1
            i += 1
        return -1

sentence = "i love eating burger"
searchWord = "burg"
solution = Solution()
print(solution.isPrefixOfWord(sentence,searchWord))