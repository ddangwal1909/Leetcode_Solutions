class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(idx,memo):
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
        
        