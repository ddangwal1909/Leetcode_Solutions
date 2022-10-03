class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        visited=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        
        
        def helper(i,j):
            nonlocal visited
            visited[i][j]=1
            curr_island.add((i-r_or,j-c_or))
            for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                if i+r<len(grid) and i+r>=0 and j+c>=0 and j+c<len(grid[0]):
                    if visited[i+r][j+c]==0 and grid[i+r][j+c]==1:
                        helper(i+r,j+c)
            return
        
        
        res=0
        main_set=set()
        curr_island=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==0:
                    r_or=i
                    c_or=j
                    curr_island=set()
                    res=1
                    helper(i,j)
                if len(curr_island)>0:
                    main_set.add(frozenset(curr_island))
        
        if res==0:
            return 0
        else:
            return len(main_set)