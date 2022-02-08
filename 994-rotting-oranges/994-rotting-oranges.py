class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        keep_track = [[True for i in range(len(grid[0]))] for j in range(len(grid))]
        
        queue=[]
        fresh=0
        empty=0
        rotten=0
        
        
        ## create a status table and check for number of rotten,fresh and empty cells
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 or grid[i][j]==2:
                    keep_track[i][j]=False
                    if grid[i][j]==2:
                        queue.append((i,j))
                        rotten+=1
                    else:
                        empty+=1
                else:
                    fresh+=1
        
        
        min_elapsed=0
        
        ## check if all cells are empty
        if empty==len(grid)*len(grid[0]):
            return 0
        
        ## check if matrix only has empty and rotten cells
        if empty+rotten == len(grid)*len(grid[0]):
            return 0
        
        
        while queue:
            if fresh==0:
                return min_elapsed
            else:
                tmp_queue=queue
                queue=[]
                ## iterate through all the rotten oranges 
                while tmp_queue:
                    curr=tmp_queue[0]
                    tmp_queue.pop(0)
                    i,j=curr
                    for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                        if 0<=(i+r)<len(keep_track) and 0<=(j+c)<len(keep_track[0]):
                            if keep_track[i+r][j+c]==True:
                                keep_track[i+r][j+c]=False
                                fresh-=1
                                queue.append((i+r,j+c))
                min_elapsed+=1
        return -1
                            
        