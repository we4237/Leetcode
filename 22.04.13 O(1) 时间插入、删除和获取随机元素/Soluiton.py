from random import choice


class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.indices={}

# 加长数组+哈希表
    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums) #补充哈希表index
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val] # 找到哈希表中index
        self.nums[index] = self.nums[-1] # val所在的位置-1
        self.indices[self.nums[index]] = index
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1)
# param_2 = obj.remove(val)
param_3 = obj.getRandom()
print(param_3)