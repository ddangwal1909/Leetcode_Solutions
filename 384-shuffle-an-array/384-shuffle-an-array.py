class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        seen = set()
        res = []
        
        for _ in range(len(self.nums)):
            num = random.choice(self.nums)
            while num in seen:
                num = random.choice(self.nums)
            seen.add(num)
            res.append(num)
        
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()