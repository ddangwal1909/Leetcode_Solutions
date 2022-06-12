class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        
        
        @lru_cache()
        def helper(curr_row,curr_col):
            
            if curr_row>=len(grid)-1:
                return grid[curr_row][curr_col]
            else:
                m_cost=math.inf
                for j in range(len(grid[0])):
                    cost=moveCost[grid[curr_row][curr_col]][j]+grid[curr_row][curr_col]+helper(curr_row+1,j)
                    m_cost=min(m_cost,cost)
                return m_cost
        
        
        mn_cost=math.inf
        
        for col in range(len(grid[0])):
            mn_cost=min(helper(0,col),mn_cost)
            
        
        return mn_cost
        