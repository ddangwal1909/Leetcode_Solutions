class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashmap={}
        
        for i in s1:
            if i not in hashmap.keys():
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        
        i,j=0,len(s1)
        
        while j<=len(s2):
            print(j)
            hashmap2={}
            
            for k in range(i,j):
                if s2[k] not in hashmap2.keys():
                    hashmap2[s2[k]]=1
                else:
                    hashmap2[s2[k]]+=1
            
            if hashmap2==hashmap:
                return True
            print(hashmap2)
            i+=1
            j+=1
        return False