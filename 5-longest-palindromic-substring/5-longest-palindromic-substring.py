class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        cache={}
        
        for i in range(len(s)):
            cache[(i,i)]=True
            
        size=1
        res=s[0]
        while size<len(s):
            left=0
            right=left+size
            
            while right<len(s):
                if s[left]==s[right] and ((right-left)==1 or ((left+1,right-1) in cache.keys())):
                    cache[(left,right)]=True
                    res=s[left:right+1]
                left+=1
                right+=1
            size+=1
        
        return res
            
            
        