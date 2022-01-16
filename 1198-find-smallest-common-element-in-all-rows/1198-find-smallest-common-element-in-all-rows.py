class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        dict={}
        ele_lst=[]
        
        for i in mat:
            for j in i:
                if j not in dict.keys():
                    dict[j]=1
                    ele_lst.append(j)
                else:
                    dict[j]+=1
        
        ele_lst.sort()
        res=-1
        for i in ele_lst:
            if dict[i]==len(mat):
                return i
        return res