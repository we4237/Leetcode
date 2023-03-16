from datashape import string


class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2 == 1:
            return n*'a'

        return (n-1)*'a'+'b'