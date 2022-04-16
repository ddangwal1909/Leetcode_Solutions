class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s = str(n)
        prod=1
        sm=0
        
        for i in s:
            prod*=int(i)
            sm+=int(i)
        
        return prod - sm
        