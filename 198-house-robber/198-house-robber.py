class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp=[0]*(len(nums)+2)
        
        for i in range(len(nums)-1,-1,-1):
            #print(dp[i+2:])
            dp[i]=nums[i]+max(dp[i+2:])
        
        return max(dp)