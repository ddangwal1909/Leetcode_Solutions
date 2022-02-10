class Solution:
    
    def binarysearch(self, nums,ele):
        l,r=0,len(nums)-1
        if len(nums)==1:
            if nums[0]==ele:
                return (True,0)
            else:
                return (False,-1)
        while l<=r:
            mid=(l+r)//2
            print(l,r,mid)
            if nums[mid]==ele:
                return (True,mid)
            elif nums[mid]<ele:
                l=mid+1
            else:
                r=mid-1
        return (False,-1)
        
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        flag,idx = self.binarysearch(nums,target)
        
        if flag==False:
            return [-1,-1]
        else:
            i=idx-1
            
            while i>=0:
                if nums[i]!=target:
                    break
                i-=1
            i+=1
            
            j = idx+1
            
            while j<len(nums):
                if nums[j]!=target:
                    break
                j+=1
            j-=1
            
            return [i,j]