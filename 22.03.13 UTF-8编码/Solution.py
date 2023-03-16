from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        MASK1,MASK2=1<<7,(1<<7)|(1<<6)

        def getBytes(num:int) -> int:
            if(num&MASK1)==0:
                return 1
            n,mask = 0,MASK1
            while num&mask:
                n+=1
                if n>4:
                    return -1
                mask >>=1  # 右移动运算符
            return n if n>=2 else -1

        index,m = 0,len(data)
        while index<m:
            n = getBytes((data[index]))
            if n < 0 or index + n > m or any((ch & MASK2) != MASK1 for ch in data[index+1:index+n]):
                # 当data在头字节后面的字节数大于等于n-1时,头字节后面的n-1个字节为当前字符的其余字节.
                # 判断每个其余字节的最高两位是否是10,如果存在一个其余字节的最高两位不是10,则data不是有效的utf8编码
                # 计算其余字节和MASK2的按位与运算结果是否等于MASK1

                return False
            index += n
        return True

if __name__ =='__main__':
    data = [197, 130, 1]
    solution = Solution()
    print(solution.validUtf8(data))


