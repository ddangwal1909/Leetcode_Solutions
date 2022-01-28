class Solution:
    
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            ways=self.climbStairs(n-1)+self.climbStairs(n-2)
            return ways