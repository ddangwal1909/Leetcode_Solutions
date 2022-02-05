class Solution:
    
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        res=values[0]
        a_i=values[0]

        for i in range(1,len(values)):
            
            res=max(values[i]-i+a_i,res)
            a_i=max(a_i,values[i]+i)
        
        return res
        