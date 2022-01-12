class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        i=len(heights)-2
        mx_curr=heights[len(heights)-1]
        res=[len(heights)-1]
        while i>=0:
            if mx_curr<heights[i]:
                res.append(i)
                mx_curr=heights[i]    
            i-=1        
        res = res[::-1]
        return res
            
        