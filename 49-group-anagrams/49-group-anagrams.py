class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap={}
        
        for i in strs:
            tmp = i
            tmp = ''.join(sorted(tmp))
            if tmp in hashmap.keys():
                hashmap[tmp].append(i)
            else:
                hashmap[tmp]=[i]
        
        res=[]
        print(hashmap)
        for j in hashmap.keys():
            res.append(hashmap[j])
        
        return res
            
        