from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        tmpExperience = 0
        Energy = sum(energy) - initialEnergy + 1 if sum(energy) - initialEnergy + 1 > 0 else 0
        for e in experience:
            if initialExperience <= e:
                boostExperience = e - initialExperience + 1
                tmpExperience += boostExperience
            else:
                boostExperience = 0
            initialExperience += boostExperience + e
        return tmpExperience + Energy

initialEnergy = 5
initialExperience = 3
energy = [1,4]
experience = [2,5]
solution = Solution()
print(solution.minNumberOfHours(initialEnergy,initialExperience, energy, experience))
