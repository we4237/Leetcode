from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n=len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0 ,0
        def dfs(node:int) -> int:
            score = 1
            sum = 1
            for ch in children[node]:
                t =dfs(ch)
                score *= t
                sum += t
            if node != 0:
                score *= n-sum
            nonlocal maxScore,cnt
            if  (maxScore == score):
                cnt += 1
            elif(maxScore<score):
                maxScore=score
                cnt = 1
            return sum;
        dfs(0)
        return cnt

if __name__ == '__main__':
    parents = [-1, 2, 0, 2, 0]
    solution = Solution()
    print(solution.countHighestScoreNodes(parents))