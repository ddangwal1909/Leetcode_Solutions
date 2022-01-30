class Solution:
    def jump(self, nums: List[int]) -> int:
        dp_mn_steps=[0]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i+1,min(i+nums[i]+1,len(nums))):
                if dp_mn_steps[j]!=0:
                    dp_mn_steps[j]=min(dp_mn_steps[j],dp_mn_steps[i]+1)
                else:
                    dp_mn_steps[j]=dp_mn_steps[i]+1
        
        return dp_mn_steps[-1]
