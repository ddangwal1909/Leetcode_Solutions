class Solution:
    
    def changeperm(self,arr):
        res=[]
        for i in range(len(arr)):
            if i%2==0:
                res.append(arr[i//2])
            else:
                res.append(arr[(len(arr)-1+i)//2])
        
        return res
    
    def checksame(self,orig,curr):
        if orig==curr:
            return True
        else:
            return False
        
    
    def reinitializePermutation(self, n: int) -> int:
        orig=[i for i in range(n)]
        curr=orig[:]
        curr=self.changeperm(curr)
        step=1
        while self.checksame(orig,curr)==False:
            step+=1
            curr=self.changeperm(curr)
        
        return step
        
        
        