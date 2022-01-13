class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        west_east_sky = [max(i) for i in grid]
        north_south_sky=[]
        for i in range(len(grid)):
            mx=grid[0][i]
            for j in range(len(grid)):
                mx = max(grid[j][i],mx)
            north_south_sky.append(mx)
        
        max_change=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]<west_east_sky[i] and grid[i][j]<north_south_sky[j]:
                    max_change+=min(west_east_sky[i],north_south_sky[j])-grid[i][j]
        
        return max_change