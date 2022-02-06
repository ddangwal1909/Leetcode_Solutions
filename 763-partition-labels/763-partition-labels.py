class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapped={}
        distinct_alpha=[]
        for i in range(len(s)):
            if s[i] not in mapped.keys():
                mapped[s[i]]=[i,i,1]
                distinct_alpha.append(s[i])
            else:
                mapped[s[i]][1]=i
                mapped[s[i]][2]+=1
        
        res=[]
        
        i=1
        tmp=mapped[s[0]][2]
        curr_min=mapped[s[0]][0]
        curr_mx=mapped[s[0]][1]
        
        while i<len(distinct_alpha):
            if mapped[distinct_alpha[i]][0]>curr_mx:
                res.append(tmp)
                curr_min=mapped[distinct_alpha[i]][0]
                curr_mx=mapped[distinct_alpha[i]][1]
                tmp=mapped[distinct_alpha[i]][2]
            else :
                tmp+=mapped[distinct_alpha[i]][2]
                curr_mx=max(mapped[distinct_alpha[i]][1],curr_mx)
            i+=1
        
        res.append(tmp)
        print(mapped)
        return res