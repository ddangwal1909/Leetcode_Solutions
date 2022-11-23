class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dp=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        dp[-1]=matrix[-1]
        
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])):
                dp[i][j]=matrix[i][j]+dp[i+1][j]
                if (j+1)<len(matrix[0]):
                    dp[i][j]=min(dp[i+1][j+1]+matrix[i][j],dp[i][j])
                if (j-1)>=0:
                    dp[i][j]=min(dp[i+1][j-1]+matrix[i][j],dp[i][j])
        print(dp)
        return min(dp[0])
                    
                
        