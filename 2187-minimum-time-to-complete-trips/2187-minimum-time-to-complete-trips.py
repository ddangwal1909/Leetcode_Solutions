class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        low, high = 0, 10**15
        
        while low<high:
            
            mid = (low+high)//2
            
            trips=0
            for i in time:
                trips+=(mid//i)
            
            if trips<totalTrips:
                low=mid+1
            else:
                high=mid
                
        return low
        
            
            
            
        
            