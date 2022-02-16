class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        
        
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return nums.index(max(nums))
        else:
            while l<=r:

                mid=(l+r)//2
                #print(mid)
                if mid==0: 
                    if nums[mid+1]<nums[mid]:
                        return 0
                    else:
                        l=mid+1
                        r=len(nums)-1
                elif mid==len(nums)-1:
                    if nums[mid-1]<nums[mid]:
                        return len(nums)-1
                    else:
                        l=0
                        r=len(nums)-2
                elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid]>=nums[mid-1] and nums[mid]<nums[mid+1]:
                    l=mid+1
                else:
                    r=mid-1
        
            return -1
        
        
                
                
                
                