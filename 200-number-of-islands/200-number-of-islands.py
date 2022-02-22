class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        
        def helper(i,j):
            
            nonlocal visited
            nonlocal grid
            
            visited[i][j]=True
            
            for row,col in [(0,-1),(0,1),(1,0),(-1,0)]:
                if 0<=i+row<len(grid) and 0<=j+col<len(grid[0]):
                    if visited[i+row][j+col] == False and grid[i+row][j+col]=='1':
                        helper(i+row,j+col)
            
            return
            
        
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==False and grid[i][j]=='1':
                    res+=1
                    helper(i,j)
                else:
                    continue
        
        return res
                    
        
        
        