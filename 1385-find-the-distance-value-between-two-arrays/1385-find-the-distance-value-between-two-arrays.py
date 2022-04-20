class Solution:
    
    def binarysearchdiff(self,ele,arr,d):
        start,end=0,len(arr)
        while start<end:
            mid = (start+end)//2
            if -d<=arr[mid]-ele<=d:
                return False
            elif (arr[mid]-ele)>d:
                end=mid
            else:
                start=mid+1
        return True
                
            
    
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt=0
        for i in arr1:
            if self.binarysearchdiff(i,arr2,d):
                cnt+=1
        
        return cnt