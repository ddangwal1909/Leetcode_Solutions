class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp=[[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i-1>=0:
                    if obstacleGrid[i-1][j]!=1 and obstacleGrid[i][j]!=1:
                        dp[i][j]+=dp[i-1][j]
                if j-1>=0:
                    if obstacleGrid[i][j-1]!=1 and obstacleGrid[i][j]!=1:
                        dp[i][j]+=dp[i][j-1]
        print(dp)
        return dp[-1][-1]