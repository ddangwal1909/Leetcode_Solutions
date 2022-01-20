class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        res=[0]*len(heights)
        stck=[heights[len(heights)-1]]
        for i in range(len(heights)-2,-1,-1):
            
            while stck and stck[-1]<heights[i]:
                res[i]+=1
                stck.pop()
            if stck:
                res[i]+=1
            stck.append(heights[i])
        
        return res
                    
        