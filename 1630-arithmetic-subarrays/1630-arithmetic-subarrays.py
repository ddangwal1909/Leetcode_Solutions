class Solution:
    
    def isarithmetic(self,arr):
        arr.sort()
        sm=sum(arr)
        if len(arr)==1:
            return True
        else:
            d=arr[1]-arr[0]
            
            for i in range(1,len(arr)):
                if arr[i]-arr[i-1]!=d:
                    return False
            
            return True            
            
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        res=[]
        for i in range(len(l)):
            #print(self.isarithmetic(nums[l[i]:r[i]+1]))
            res.append(self.isarithmetic(nums[l[i]:r[i]+1]))
        
        return res
            
        
        
       ## 0 -2 -6 -8
        ##4*
        
        0 -2 -6 -8
    
        