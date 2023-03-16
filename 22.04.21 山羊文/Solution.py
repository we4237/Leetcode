class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        n = len(sentence)
        i,cnt = 0,1
        words=list()

        while i < n:
            j = i

            while j < n and sentence[j] != " ":
                j += 1

            cnt += 1
            if sentence[i] in vowels:
                words.append(sentence[i:j]+"m"+"a"*cnt)
            else:
                words.append(sentence[i+1:j]+sentence[i]+"m"+"a"*cnt)

            i = j + 1

        return " ".join(words)

sentence = "I speak Goat Latin"
solution = Solution()
print(solution.toGoatLatin(sentence))