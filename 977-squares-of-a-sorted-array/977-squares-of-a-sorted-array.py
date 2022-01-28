class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i,j=0,len(nums)-1
        break_type=0
        res=[]
        while True and i<j:
            
            if nums[j]<0:
                break_type=1
                break
            
            if nums[i]>0:
                break_type=0
                break
                
            if abs(nums[i])>abs(nums[j]):
                res.insert(0,nums[i]*nums[i])
                i+=1
            else:
                res.insert(0,nums[j]*nums[j])
                j-=1
                
        if break_type==0:
            for k in range(j,i-1,-1):
                res.insert(0,nums[k]*nums[k])
        else:
            for k in range(i,j+1):
                res.insert(0,nums[k]*nums[k])
                
        
        return res
            
                
            
            
        