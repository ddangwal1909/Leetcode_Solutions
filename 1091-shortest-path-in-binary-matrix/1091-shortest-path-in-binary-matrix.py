class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(1,0),(-1,-1),(1,1),(0,1),(0,-1),(-1,1),(1,-1)]
        
        def getneighbours(i,j):
            
            lst = []
            
            for r,c in directions:
                if 0<=i+r<len(grid) and 0<=j+c<len(grid[0]):
                    if grid[i+r][j+c]==0:
                        lst.append((i+r,j+c))
            
            return lst
        
        
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        
        queue = [(0,0)]
        
        grid[0][0]=1
        
        while queue:
            curr = queue.pop(0)
            distance = grid[curr[0]][curr[1]]
            if curr[0]==len(grid)-1 and curr[1]==len(grid[0])-1:
                    return grid[curr[0]][curr[1]]   
            for row,col in getneighbours(curr[0],curr[1]):
                grid[row][col]=distance+1
                queue.append((row,col))
    
        return -1
            
                    
                        
                
                
                
                
                