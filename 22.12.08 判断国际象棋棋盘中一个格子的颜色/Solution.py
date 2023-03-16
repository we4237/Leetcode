class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0])-ord('a')+1+ord(coordinates[1]) ) % 2==1
coordinates = "a1"
solution = Solution()
print(solution.squareIsWhite(coordinates))