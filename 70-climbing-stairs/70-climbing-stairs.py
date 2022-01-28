class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*(n+1)
        arr[0]=0
        arr[1]=1
        if n>1:
            arr[2]=2
        for i in range(3,n+1):
            arr[i]=arr[i-1]+arr[i-2]
        
        return arr[-1]
    
    
    
    
    
    ### Recursion with memoization
    '''@lru_cache(None)
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
    '''
        