class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap={}
        lst=[]
        res=[]
        for i in nums:
            if i in hashmap.keys():
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in hashmap.keys():
            lst.append((i,hashmap[i]))
        
        
        lst.sort(key=lambda x: x[1],reverse=True)
        
        for p in range(k):
            res.append(lst[p][0])
        
        return res
            