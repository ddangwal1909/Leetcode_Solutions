class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        last_dp=triangle[-1]
        new_dp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            new_dp=[]
            for j in range(len(last_dp)-1):
                new_dp.append(triangle[i][j]+min(last_dp[j],last_dp[j+1]))
            #print(last_dp,new_dp)
            last_dp=new_dp
        #print(new_dp)
        return new_dp[0]