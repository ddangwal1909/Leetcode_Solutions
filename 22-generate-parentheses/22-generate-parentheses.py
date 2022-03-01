class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res=[]
        
        def helper(l,r,curr):
            
            if len(curr)==2*n:
                res.append(''.join(curr))
                return
            
            if l<=n:
                curr.append('(')
                l+=1
                helper(l,r,curr[:])
                curr.pop()
                l-=1
            if r<l:
                curr.append(')')
                r+=1
                helper(l,r,curr[:])
                curr.pop()
                r-=1
            return
        
        helper(1,1,[])
        
        return res
                
                