class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch:str) -> int:
            ans,left,sum = 0,0,0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch # sum 记录区间中另一种字符的数量
                while sum>k:
                    sum -=answerKey[left] != ch
                    left += 1
                ans = max(ans,right-left+1)
            return ans
        return max(maxConsecutiveChar('T'),maxConsecutiveChar('F'))

answerKey = "TTFF"
k = 2
solution = Solution()
print(solution.maxConsecutiveAnswers(answerKey,k))
