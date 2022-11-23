class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        def cmp(a, b):
            return (a > b) - (a < b) 
        
        res, [i, j], [x, y] = 0, startPos, homePos
        while i != x:
            i += cmp(x, i)
            res += rowCosts[i]
        while j != y:
            j += cmp(y, j)
            res += colCosts[j]
        
            
        return res        
        
        
        
        
        