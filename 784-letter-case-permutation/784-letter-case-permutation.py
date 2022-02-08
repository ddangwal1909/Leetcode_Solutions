class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res =[]
        
        def helper(curr,k,orig):
            print(curr)
            if k==len(orig):
                res.append(curr)
                return
            else:
                if (orig[k]>='A' and orig[k]<='Z'):
                    curr=curr+orig[k]
                    helper(curr,k+1,orig)
                    curr=curr[:len(curr)-1]
                    curr+=orig[k].lower()
                    helper(curr,k+1,orig)
                elif (orig[k]>='a' and orig[k]<='z'):
                    curr=curr+orig[k]
                    helper(curr,k+1,orig)
                    curr=curr[:len(curr)-1]
                    curr+=orig[k].upper()
                    helper(curr,k+1,orig)
                else:
                    curr=curr+orig[k]
                    helper(curr,k+1,orig)
            return
                
        helper('',0,s)
        
        print(res)
        return res