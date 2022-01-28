class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(None)
        def helper(idx):
            if idx>=len(cost):
                return 0
            else:
                return cost[idx]+min(helper(idx+1),helper(idx+2))
            
        
        res=min(helper(0),helper(1))
        return res