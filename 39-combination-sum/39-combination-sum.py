class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        res=[]
        
        def helper(curr,sm):
            curr.sort()
            if sm==target and curr[:] not in res:
                res.append(curr[:])
                return
            
            if sm>target:
                return
            
            for i in candidates:
                curr.append(i)
                sm+=i
                helper(curr[:],sm)
                sm-=i
                curr.pop(len(curr)-1)
            
            return
        
        helper([],0)
        
        return res
                
        