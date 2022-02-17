class Solution:       
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        orig_hash = [0]*27
        
        curr_hash = [0]*27
        
        if len(p)>len(s) or len(p)==0 or len(s)==0:
            return []
        
        for i in p:
            orig_hash[ord(i)-ord('a')]+=1
        
        i,j=0,len(p)
        
        for k in range(i,j):
            curr_hash[ord(s[k])-ord('a')]+=1
            
        i=0
        j=len(p)-1
        res=[]
        
        while j<len(s):
            if curr_hash==orig_hash:
                res.append(i)
            curr_hash[ord(s[i])-ord('a')]-=1
            i+=1
            j+=1
            if j<len(s):
                curr_hash[ord(s[j])-ord('a')]+=1
        
        return res