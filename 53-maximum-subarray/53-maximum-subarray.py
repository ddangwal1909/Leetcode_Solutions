class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalmx = -1*math.inf
        tmp=0
        for i in range(len(nums)):
            tmp+=nums[i]
            if tmp<nums[i]:
                tmp = nums[i]
            globalmx = max(globalmx,tmp)
        return max(globalmx,tmp)
            
        