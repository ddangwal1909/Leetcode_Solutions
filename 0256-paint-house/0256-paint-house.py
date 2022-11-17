class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        def helper(idx,color,memo):
            if idx>=len(costs):
                return 0
            if memo[idx][color]!=-1:
                return memo[idx][color]
            else:
                if color==0:
                    memo[idx][color]=costs[idx][color]+min(helper(idx+1,1,memo[:]),helper(idx+1,2,memo[:]))
                elif color==1:
                    memo[idx][color]=costs[idx][color]+min(helper(idx+1,0,memo[:]),helper(idx+1,2,memo[:]))
                else:
                    memo[idx][color]=costs[idx][color]+min(helper(idx+1,0,memo[:]),helper(idx+1,1,memo[:]))
            return memo[idx][color]
                    
                
                
        memo=[[-1 for i in range(len(costs[0]))] for i in range(len(costs))]
        res=min(helper(0,0,memo[:]),helper(0,1,memo[:]),helper(0,2,memo[:]))
        print(memo)
        return res