class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited=[]
        
        mx=0
        @lru_cache(None)
        def helper(i,j):
            
            tmp=grid[i][j]
            for r,c in [(0,1),(1,0),(0,-1),(-1,0)]:
                if (i+r)>=0 and (i+r)<len(grid) and (j+c)>=0 and (j+c)<len(grid[0]):
                    if grid[i+r][j+c]==1 and (i+r,j+c) not in visited:
                        visited.append((i+r,j+c))
                        tmp = tmp+helper(i+r,j+c)
            
            return tmp
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    visited.append((i,j))
                    mx = max(mx,helper(i,j))
        return mx
                        