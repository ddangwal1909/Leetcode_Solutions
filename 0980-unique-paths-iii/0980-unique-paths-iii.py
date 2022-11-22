class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        res=0
        def helper(i,j,visited,te,v_arr):
            nonlocal res
            v_arr.append((i,j))
            #print(v_arr)
            te-=1
            if grid[i][j]==2:
                if te==0:
                    res+=1
                    #print(v_arr)
                    return
                else:
                    return
            
            for r,c in [(0,-1),(0,1),(-1,0),(1,0)]:
                if 0<=i+r<len(grid) and 0<=j+c<len(grid[0]):
                    if visited[i+r][j+c]==False:
                        visited[i+r][j+c]=True
                        helper(i+r,j+c,visited[:],te,v_arr[:])
                        visited[i+r][j+c]=False
            return
        
        s_i=-1
        s_j=-1
        v=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        total_empty=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    s_i=i
                    s_j=j
                    total_empty+=1
                elif grid[i][j]==-1:
                    v[i][j]=True
                else:
                    total_empty+=1
        #print(total_empty)
        v[s_i][s_j]=True
        helper(s_i,s_j,v.copy(),total_empty,[])
        
        
        return res