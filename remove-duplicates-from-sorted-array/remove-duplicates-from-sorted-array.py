class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1  
        k=1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                j+=1
                k+=1
        
        return k