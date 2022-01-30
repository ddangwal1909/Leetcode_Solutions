class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jmp_dp=[False for i in range(len(nums))]
        
        jmp_dp[-1]=True
        
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,min(len(nums),i+1+nums[i])):
                if jmp_dp[j]==True:
                    jmp_dp[i]=True
                    break
        
        if jmp_dp[0]==True:
            return True
        else:
            return False
        