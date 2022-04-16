class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        low,high=0,len(nums)-1
        
        
        if len(nums)==1:
            if nums[0]<target:
                return 1
            else:
                return 0
        
        elif nums[0]>=target:
            return 0
        
        elif nums[-1]<target:
            return len(nums)
        
        else:      
            while low<=high:    
                mid=(low+high)//2
                if nums[mid]<target and nums[mid+1]>=target:
                    res=mid+1
                    break
                elif nums[mid]<target and nums[mid+1]<target:
                    low=mid+1
                else:
                    high=mid
            return res
            
        
        
        