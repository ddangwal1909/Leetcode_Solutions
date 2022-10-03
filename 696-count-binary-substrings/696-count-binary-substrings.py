class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev=0
        curr=1
        res=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                curr+=1
            else:
                res+=min(curr,prev)
                prev=curr
                curr=1
        res+=min(curr,prev)
        return res
                
        