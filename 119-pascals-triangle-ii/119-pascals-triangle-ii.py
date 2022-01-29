class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mat=[[] for i in range(40)]
        mat[0]=[1]
        mat[1]=[1,1]
        
        for i in range(2,40):
            mat[i].append(1)
            for j in range(1,len(mat[i-1])):
                mat[i].append(mat[i-1][j-1]+mat[i-1][j])
            mat[i].append(1)
        
        return mat[rowIndex]
        
        
        