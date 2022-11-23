class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        dp=points[0]
                
        for i in range(1,len(points)):
            left=[0]*len(points[0])
            right=[0]*len(points[0])
            dp_new=[]
            for j in range(len(points[0])):
                if j==0:
                    left[j]=dp[j]
                else:
                    left[j]=max(dp[j],left[j-1]-1)
            
            for j in range(len(points[0])-1,-1,-1):
                if j==len(points[0])-1:
                    right[j]=dp[j]
                else:
                    right[j]=max(dp[j],right[j+1]-1)
            
            for j in range(len(points[0])):
                dp_new.append(points[i][j]+max(left[j],right[j]))
            
            dp=dp_new[:]
            
                
        
        return max(dp)