class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [False for i in range(len(isConnected))]
        
        def helper(row):
            
            visited[row]=True
            for j in range(len(isConnected[row])):
                if isConnected[row][j]==1 and visited[j]==False:
                    helper(j)
            return
            
            
        
        res=0
        for i in range(len(isConnected)):
            if visited[i]==False:
                res+=1
                helper(i)
        
        return res