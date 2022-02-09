class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            tmp = n&1
            
            if tmp==1:
                res=(res<<1)|1
            else:
                res=(res<<1)
            n=n>>1
        
        return res
        