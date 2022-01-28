# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low,high=1,n
        
        if isBadVersion(low)==True:
            return low
        
        else:
            
            while low<=high:
                
                #print(mid)
                mid=(low+high)//2
                
                curr=isBadVersion(mid)
                prev=isBadVersion(mid-1)
                
                if curr==True and prev==False:
                    res=mid
                    break
                elif curr==True and prev==True:
                    high=mid
                else:
                    low=mid+1
            return res
        
        