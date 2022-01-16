class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        l_r_lst=[arr[0]]
        #r_l_lst=[arr[-1]]
        
        for i in range(1,len(arr)):
            l_r_lst.append(l_r_lst[i-1]^arr[i])
        
        res=[]
        for i in range(len(queries)):
            if queries[i][0]-1<0:
                res.append(l_r_lst[queries[i][1]])
            else:
                res.append(l_r_lst[queries[i][0]-1]^l_r_lst[queries[i][1]])
        
        return res
        
        
        