

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        haxi = dict()
        cur = 'a'
        key = key.replace(' ','')

        for char in key:
            if char not in haxi: #一个字母只遍历一次
                haxi[char] = cur
                cur = chr(ord(cur)+1) #通过ord()实现字母增加
        res = "".join(haxi.get(c, " ")for c in message)

        return res


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
solution = Solution()
print(solution.decodeMessage(key,message))

