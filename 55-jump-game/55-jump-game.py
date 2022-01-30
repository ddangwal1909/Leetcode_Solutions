class Solution:
    
    def canJump(self, nums: List[int]) -> bool:        
        max_reach = 0
        for i in range(len(nums)):
            if i <= max_reach:                
                max_reach = max(max_reach,i+nums[i])
        return max_reach >= len(nums) - 1	
    
    '''
    def canJump(self, nums: List[int]) -> bool:
        
        jmp_dp=[False for i in range(len(nums))]
        
        jmp_dp[-1]=True
        
        for i in range(len(nums)-2,-1,-1):
            if jmp_dp[i]==False:
                for j in range(i+1,min(len(nums),i+1+nums[i])):
                    if jmp_dp[j]==True:
                        jmp_dp[i]=True
                        break
        
        if jmp_dp[0]==True:
            return True
        else:
            return False
        '''