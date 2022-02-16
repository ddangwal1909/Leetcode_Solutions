class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<mn:
                mn=nums[i]
                break
        return mn
            
        