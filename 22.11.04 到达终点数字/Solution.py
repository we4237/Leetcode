class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = road = 0
        while road < target or (target-road) % 2:
            n += 1
            road += n
        return n

target = 3
solution = Solution()
print(solution.reachNumber(target))