class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_tmp={}
        dict_tmp_2={}
        for i in arr:
            if i not in dict_tmp.keys():
                dict_tmp[i]=1
            else:
                dict_tmp[i]+=1
                
        flag=True
        frst=True
        
        for i in dict_tmp.keys():
            if dict_tmp[i] in dict_tmp_2.keys():
                flag=False
            else:
                dict_tmp_2[dict_tmp[i]]=1
        return flag
        