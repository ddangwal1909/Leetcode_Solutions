# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        i,j=0,100000
        res=-1
        while i<j:
            mid = (i+j)//2
            if reader.get(mid)==2**31-1:
                j=mid
                continue
            elif target==reader.get(mid):
                res=mid
                break
            elif target<reader.get(mid):
                j=mid
            else:
                i=mid+1
        
        return res
                
                
                
        