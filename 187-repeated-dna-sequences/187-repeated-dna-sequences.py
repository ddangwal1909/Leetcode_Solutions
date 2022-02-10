class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dna={}
        res=[]
        i=0
        j=10
        
        if len(s)==10:
            return []
        while j<=len(s):
            if s[i:j] in dna.keys():
                dna[s[i:j]]+=1
                if dna[s[i:j]]==2:
                    res.append(s[i:j])
            else:
                dna[s[i:j]]=1
            i+=1
            j+=1
        if len(list(dna.keys()))==1:
            res=[list(dna.keys())[0]]
        
        return res
                    
            
        
        