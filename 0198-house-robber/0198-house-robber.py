class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        dp=[0]*len(nums)
        dp[-1]=nums[-1]
        dp[-2]=nums[-2]
        
        for i in range(len(nums)-3,-1,-1):
            mx_curr=-100000
            for j in range(i+2,len(nums)):
                mx_curr=max(mx_curr,dp[j]+nums[i])
            dp[i]=mx_curr

        return max(dp)
                
        
'''     def helper(idx,memo):
            if idx>=len(nums):
                return 0
            if memo[idx]!=-1:
                return memo[idx]
            else:
                mx_curr=max(nums[idx]+helper(idx+2,memo),helper(idx+1,memo))
                memo[idx]=mx_curr
                return mx_curr
            
        memo=[-1]*len(nums)
        return helper(0,memo)
'''     