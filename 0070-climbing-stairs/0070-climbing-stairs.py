class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+2)
        dp[n]=1
        for i in range(n-1,-1,-1):
            dp[i]=dp[i+1]+dp[i+2]
            print(dp)
        
        return dp[0]
    
        