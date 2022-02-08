class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp=[]
        for i in range(len(triangle)):
            tmp=[]
            for j in range(len(triangle[i])):
                tmp.append(math.inf)
            dp.append(tmp)
        
        
        dp[len(dp)-1]=triangle[len(triangle)-1]
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[i][j]=triangle[i][j]+min(dp[i+1][j],dp[i+1][j+1])
        
        return dp[0][0]
    