class Solution:
    
    
    def binsearch(self,array,target):
        
        i,j=0,len(array)-1
        
        while i<=j:
            mid = (i+j)//2
            if array[mid]==target:
                return True
            elif array[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return False
            
                
        
    
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0
        
        if len(matrix)==1:
            return self.binsearch(matrix[0],target)
        
        elif matrix[len(matrix)-1][len(matrix[0])-1]<target:
            return False
        else:
            
            while i<len(matrix):
                print(i)
                if matrix[i][0]>target:
                    break
                if matrix[i][-1]<target:
                    i+=1
                else:
                    print(i)
                    if self.binsearch(matrix[i],target)==True:
                        return True
                    else:
                        i+=1
            return False
                    
                    
                
                
            
        