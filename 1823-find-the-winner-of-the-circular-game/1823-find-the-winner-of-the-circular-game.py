class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lst=[i for i in range(1,n+1)]
        
        
        def helper(arr,n,k,curr):
            
            if n==1:
                return arr
            else:
                curr=((curr+k-1)%n)
                #print(arr[curr])
                #print(arr)
                arr.pop(curr)
                #print(arr[curr_idx+1])
                print('curr_idx',curr)
                return helper(arr,n-1,k,curr)
            
        res = helper(lst,n,k,0)
        
        return res[0]
        
            