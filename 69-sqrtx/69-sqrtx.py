class Solution:
    def mySqrt(self, x: int) -> int:
        
        start,end=1,x//2
        md=1
        
        if x==0:
            return 0
        
        while start<=end:
            md = (start+end)//2
            
            if md*md==x:
                return md
            elif md*md>x and (md-1)*(md-1)<x:
                return md-1
            elif md*md>x:
                end=md-1
            else:
                start=md+1
        
        return md