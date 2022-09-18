class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        hashmap={
            'M':{
                'max':-1,
                 'freq':0
            },
            'P':{
                'max':-1,
                'freq':0
            },
            'G':
            {
                'max':-1,
                'freq':0
            }
        }
        for i in range(len(garbage)):
            for j in garbage[i]:
                hashmap[j]['max']=i
                hashmap[j]['freq']+=1
                
        sm_arr=[0]
        for j in range(len(travel)):
            sm_arr.append(sm_arr[-1]+travel[j])
        res=0
        for k in hashmap.keys():
            if hashmap[k]['max']!=-1:
                res+=sm_arr[hashmap[k]['max']]+hashmap[k]['freq']
        
        return res
             
        