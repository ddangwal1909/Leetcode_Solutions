class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(idx,memo,nums):
            if idx>=len(nums):
                return 0
            if memo[idx]!=-1:
                return memo[idx]
            else:
                mx_curr=max(nums[idx]+helper(idx+2,memo,nums),helper(idx+1,memo,nums))
                memo[idx]=mx_curr
                return mx_curr
            
        memo=[-1]*(len(nums)-1)
        memo1=[-1]*(len(nums)-1)
        if len(nums)<=3:
            return max(nums)
        return max(helper(0,memo,nums[:-1]),helper(0,memo1,nums[1:]))