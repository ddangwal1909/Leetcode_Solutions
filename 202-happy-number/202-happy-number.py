class Solution:
    
    def getss(self,n):
        curr=0
        while n>0:
            tmp=n%10
            n=int(n/10)
            curr+=(tmp**2)
        return curr

    
    def isHappy(self, n: int) -> bool:
        hash=set()
        while n!=1 and n not in hash:
            hash.add(n)
            n=self.getss(n)
        
        return n==1