class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        mat=[[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                mat[i][j]=min(rowSum[i],colSum[j])
                colSum[j]-=mat[i][j]
                rowSum[i]-=mat[i][j]
        
        return mat
        