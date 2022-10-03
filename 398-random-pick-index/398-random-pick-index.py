import random
class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap={}
        for i in range(len(nums)):
            if nums[i] not in self.hashmap:
                self.hashmap[nums[i]]=[]
            self.hashmap[nums[i]].append(i)
        
            
        
    def pick(self, target: int) -> int:
        idx=random.randint(0, len(self.hashmap[target])-1)
        return self.hashmap[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)