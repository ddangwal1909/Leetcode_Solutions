class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        def dfs(start,curr):
            if curr[:] not in res:
                res.append(curr[:])
            
            for i in range(start,len(nums)):
                curr.append(nums[i])                
                dfs(i+1,curr[:])
                curr.pop(len(curr)-1)
            
            return
        

        
        dfs(0,[])
        
        
        
        return res
        
            