class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dp = [[math.inf for i in range(len(mat[0]))] for j in range(len(mat))]
        
        ## top-bottom left to right
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    if i==0 and j>0:
                        dp[i][j]=min(1+dp[i][j-1],dp[i][j])
                    elif i>0 and j==0:
                        dp[i][j] = min(dp[i][j],1+dp[i-1][j])
                    elif i>0 and j>0:
                        dp[i][j]=min(1+dp[i-1][j],1+dp[i][j-1])
                    else:
                        continue
        print(dp)
        
        ## bottom-top right to left
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    if i==len(mat)-1 and j<len(mat[0])-1:
                        dp[i][j]=min(dp[i][j],1+dp[i][j+1])
                    elif i<len(mat)-1 and j==len(mat[0])-1:
                        dp[i][j]=min(1+dp[i+1][j],dp[i][j])
                    elif i<len(mat)-1 and j<len(mat[0])-1:
                        dp[i][j]=min(1+dp[i+1][j],1+dp[i][j+1],dp[i][j])
                    else:
                        continue
        
                        
        
        print(dp)
        
        return dp
        