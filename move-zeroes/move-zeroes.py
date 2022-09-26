class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i,j=0,0
        
        if len(nums)==0 or len(nums)==1:
            return nums
        
        else:
            
            while i<=len(nums)-1 and j<=len(nums)-1:
                if nums[i]==0 and nums[j]!=0 and i<=j:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    i+=1
                    j+=1
                    
                elif nums[i]==0 and nums[j]==0 and i<=j:
                    j+=1
                    continue
                else:
                    i+=1
                    j+=1
            
            return nums