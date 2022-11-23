class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp=[[10000000000 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        dp[-1]=grid[-1]
        
        for i in range(len(grid)-2,-1,-1):
            k=sorted(dp[i+1])
            for j in range(len(grid[0])):
                if dp[i+1].index(min(dp[i+1]))==j:    
                    dp[i][j]=grid[i][j]+k[1]
                else:
                    dp[i][j]=grid[i][j]+k[0]

        #print(dp)
        return min(dp[0])
    
 