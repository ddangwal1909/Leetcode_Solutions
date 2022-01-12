class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        for i in range(rows):
            curr_row=rows-i-1
            curr_col=0
            tmp_lst=[]
            
            ## get elements in a list
            while(curr_row<rows and curr_col<cols):
                tmp_lst.append(mat[curr_row][curr_col])
                curr_row+=1
                curr_col+=1
                
            tmp_lst.sort()
            j=0
            curr_row=rows-i-1
            curr_col=0
            while(curr_row<rows and curr_col<cols):
                mat[curr_row][curr_col]=tmp_lst[j]
                curr_row+=1
                curr_col+=1
                j+=1
        
        for i in range(1,cols):
            curr_row=0
            curr_col=i
            tmp_lst=[]
            
            ## get elements in a list
            while(curr_row<rows and curr_col<cols):
                tmp_lst.append(mat[curr_row][curr_col])
                curr_row+=1
                curr_col+=1
                
            tmp_lst.sort()
            j=0
            curr_row=0
            curr_col=i
            while(curr_row<rows and curr_col<cols):
                print(curr_row,curr_col)
                mat[curr_row][curr_col]=tmp_lst[j]
                curr_row+=1
                curr_col+=1
                j+=1
        
        return mat
                
            
            
            
        