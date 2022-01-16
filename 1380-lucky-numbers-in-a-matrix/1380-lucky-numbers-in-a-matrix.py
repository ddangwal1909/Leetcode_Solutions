class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mn_row=[min(matrix[i]) for i in range(len(matrix))]
        
        mx_col=[]
        for i in range(len(matrix[0])):
            tmp_mx=-1
            for j in range(len(matrix)):
                tmp_mx=max(tmp_mx,matrix[j][i])
            mx_col.append(tmp_mx)
        
        mn_row.sort()
        mx_col.sort()
        
        i,j=0,0
        res=[]
        while i<len(mn_row) and j<len(mx_col):
            if mn_row[i]==mx_col[j]:
                res.append(mn_row[i])
                i+=1
                j+=1
            elif mn_row[i]<mx_col[j]:
                i+=1
            else:
                j+=1
        
        return res
        