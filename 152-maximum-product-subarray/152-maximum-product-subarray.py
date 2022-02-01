class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far=nums[0]
        min_so_far=nums[0]
        result=max_so_far
        
        for i in range(1,len(nums)):
            temp_max=max_so_far
            max_so_far=max(nums[i],min_so_far*nums[i],max_so_far*nums[i])
            min_so_far=min(nums[i],min_so_far*nums[i],temp_max*nums[i])
            
            result=max(max_so_far,result)
        
        return result
            