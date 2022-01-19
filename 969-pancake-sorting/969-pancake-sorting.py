class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
    
        arr_sorted=sorted(arr[:])
        k=len(arr_sorted)-1
        res=[]
        while k>0:
           ## print(arr)
            idx=arr.index(arr_sorted[k])
####print(idx)
            #print()
            arr=arr[:idx+1][::-1]+arr[idx+1:]
            res.append(idx+1)
            arr=arr[:k+1][::-1]+arr[k+1:]
            res.append(k+1)
         ##   print(arr)
            k-=1
        return res
            