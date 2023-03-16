from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack_right = [] # 用于存碰撞后向右的行星
        stack_left = []  # 用于存碰撞后向左的行星
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack_right.append(asteroids[i])
            else:
                adding = True

                while stack_right:
                    cur_right = stack_right.pop()
                    if asteroids[i]+cur_right > 0 : # 右边胜,左边爆炸
                        stack_right.append(cur_right)
                        break
                    elif asteroids[i]+cur_right < 0: # 左边胜
                        continue
                    else: #一样大,同归于尽
                        adding = False
                        break
                if not stack_right and adding: # 如果右边空了,并且还没有同归于尽,那么行星直接加入stack_left
                    stack_left.append(asteroids[i])

        return stack_left + stack_right

asteroids = [5,10,-5]
solution = Solution()
print(solution.asteroidCollision(asteroids))