class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        @lru_cache(None)
        def helper(bot1,bot2,row):
            if bot1<0 or bot2<0 or bot1>=cols or bot2>=cols or row>=rows:
                return -1
            else:
                mx_pick=0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        mx_pick=max(mx_pick,helper(bot1+i,bot2+j,row+1))
                        
                if bot1!=bot2:
                    mx_pick+=grid[row][bot1]+grid[row][bot2]
                else:
                    mx_pick+=grid[row][bot1]
                return mx_pick

        res=helper(0,cols-1,0)
        return res