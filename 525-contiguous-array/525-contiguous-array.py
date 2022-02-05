class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        ## convert all 0s to 1s
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        
        
        ## now check if sum was seen earlier
        
        hashmap={}
        sm=0
        mx=0
        hashmap[0]=-1
        for i in range(len(nums)):
            
            sm+=nums[i]
            
            if sm in hashmap.keys():
                mx=max(mx,i-hashmap[sm])
            
            else:
                hashmap[sm]=i
        
        if sm==0:
            mx=len(nums)
            
        return mx
            
        
        