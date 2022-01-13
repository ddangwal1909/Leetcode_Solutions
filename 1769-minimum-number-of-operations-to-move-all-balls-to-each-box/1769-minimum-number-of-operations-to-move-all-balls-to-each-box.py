class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        
        
        
        '''
        O(N^2) solution
        ## initializing 2D array to keep track of operations
        mat = [[0 for i in range(len(boxes))] for j in range(len(boxes))]
        print(sum(mat[0]))
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                mat[i][j]=int(boxes[j])*abs(i-j)
        
        res=[]
        for i in range(len(boxes)):
            res.append(sum(mat[i]))
        '''
        
        
        nonzero_idx = [i for i in range(len(boxes)) if boxes[i]=='1']
        
        res=[]
        for i in range(len(boxes)):
            ops=0
            for j in nonzero_idx:
                ops+=abs(i-j)
            
            res.append(ops)
        return res
        