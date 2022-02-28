class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
        res=[]
        def helper(start,curr,sm):
            
            if sm==target:
                res.append(curr[:])
                return 
            
            if sm>target or start>=len(candidates):
                return
            
            
            
            sm+=candidates[start]
            curr.append(candidates[start])
            helper(start+1,curr[:],sm)
            sm-=candidates[start]
            curr.pop(len(curr)-1)
            
            while start+1<len(candidates) and candidates[start]==candidates[start+1]:
                start+=1
            
            helper(start+1,curr[:],sm)
                
            
            return
        
        
        helper(0,[],0)
        
        return res