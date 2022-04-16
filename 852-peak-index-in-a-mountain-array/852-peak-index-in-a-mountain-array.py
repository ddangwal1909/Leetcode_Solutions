class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        start,end=0,len(arr)-1
        
        while True:
            md = (start+end)//2
            if arr[md-1]<arr[md] and arr[md]>arr[md+1]:
                return md
            elif arr[md]>arr[md-1] and arr[md]<arr[md+1]:
                start=md
            else:
                end=md
        return -1