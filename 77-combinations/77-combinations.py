class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        
        def helper(k_tmp,curr,last_mn,n):
            nonlocal res
            nonlocal k
            if len(curr)==k:
                print(curr)
                res.append(curr[:])
            for j in range(last_mn,n+1):
                curr.append(j)
                helper(k_tmp-1,curr,j+1,n)
                curr.pop()
        
        res=[]
        helper(k,[],1,n)
        
        print(res)
        return res
                
        