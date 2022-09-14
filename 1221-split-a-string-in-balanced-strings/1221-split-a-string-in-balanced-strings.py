class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        hash={'R':-1,'L':1}
        res=0
        curr=0
        for i in range(len(s)):
            curr+=hash[s[i]]
            if curr==0:
                res+=1
        return res