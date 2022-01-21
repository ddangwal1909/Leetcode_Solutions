class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        @lru_cache(None)
        def helper(row,col):
            if row>=len(matrix):
                return 0
            else:
                mn_step=10000000
                for j in [-1,0,1]:
                    if col+j<len(matrix[0]) and col+j>=0:
                        mn_step=min(mn_step,helper(row+1,col+j))
                
                res=mn_step+matrix[row][col]
                return res
        
        mn_res=100000000
        for i in range(0,len(matrix[0])):
            mn_res=min(mn_res,helper(0,i))
        
        return mn_res
    
        