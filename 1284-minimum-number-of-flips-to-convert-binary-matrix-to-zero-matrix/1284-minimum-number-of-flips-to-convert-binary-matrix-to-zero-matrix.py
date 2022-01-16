class Solution:
    def __init__(self):
        self.flag=0
        self.mn_moves=100000
    
    def checkallzeroes(self,mat):
        res = sum([sum(mat[i]) for i in range(len(mat))])
        if res==0:
            return True
        else:
            return False
    
    
    def flipper(self,mat,i,j):
        
        for k in [(i,j),(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if k[0]>=0 and k[0]<len(mat) and k[1]>=0 and k[1]<len(mat[0]):
                mat[k[0]][k[1]]^=1
        return mat
         
        
    def helper(self,mat,pos,moves):        
        if self.checkallzeroes(mat):
            self.flag=1
            self.mn_moves=min(self.mn_moves,moves)
            return
        
        for i in range(len(pos)):
            x,y=pos[i]
            self.flipper(mat,x,y)
            self.helper(mat,pos[i+1:],moves+1)
            self.flipper(mat,x,y)
        
    
    def minFlips(self, mat: List[List[int]]) -> int:
        pos=[(i,j) for i in range(len(mat)) for j in range(len(mat[0]))]
        self.helper(mat,pos,0)
        
        if self.flag==1:
            return self.mn_moves
        else:
            return -1
        
        