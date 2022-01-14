class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        visited=[]
        obstacles=0
        for i in range(len(grid)):
            tmp=[]
            for j in range(len(grid[i])):
                if grid[i][j]==0 or grid[i][j]==2 or grid[i][j]==1:
                    tmp.append(False)
                    if grid[i][j]==1:
                        start_i=i
                        start_j=j
                else:
                    if grid[i][j]==-1:
                        obstacles+=1
                    tmp.append(True)
            visited.append(tmp)
        
        print(start_i,start_j)
        total_non_obs = len(grid)*len(grid[0]) - obstacles
        ##print(total_non_obs)
        
        ways=0
        
        def backtrack(grid,i,j,remain):
            nonlocal ways
            remain-=1
            #v=visited
            print((i,j),(remain))
            #print(v)
            if grid[i][j]==2 and remain==0:
                ways+=1
                print(ways)
                return
            
            else:
                
                ## mark visited
                tmp=grid[i][j]
                grid[i][j]=-4
                for row,col in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if (i+row<len(grid) and i+row>=0) and (j+col<len(grid[0]) and j+col>=0) and grid[i+row][j+col]>=0:
                        backtrack(grid,i+row,j+col,remain)
                    else:
                        continue
                grid[i][j]=tmp
            return
        
        backtrack(grid,start_i,start_j,total_non_obs)
        return ways