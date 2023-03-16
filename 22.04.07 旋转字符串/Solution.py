class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        data=len(s)
        target=len(goal)

        if data != target:
            return False
        for i in range(data):
            for j in range(data):
                if s[(i+j) % target] !=goal[j]:
                    break
            else:
                return True

        return False

if __name__ =='__main__':
    s,goal= "abcde","cdeab"
    solution=Solution()
    print(solution.rotateString(s,goal))

