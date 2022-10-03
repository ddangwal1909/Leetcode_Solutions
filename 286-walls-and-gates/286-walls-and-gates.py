class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        mx=2147483647
        
        def helper(i,j,curr_len):
            if rooms[i][j]!=0:
                curr_len+=1
                rooms[i][j]=curr_len
                
            for r,c in [(0,-1),(0,1),(1,0),(-1,0)]:
                if 0<=i+r<len(rooms) and 0<=j+c<len(rooms[0]):
                    if rooms[i+r][j+c]!=0 and rooms[i+r][j+c]!=-1:  
                        if (rooms[i+r][j+c]==mx or (rooms[i+r][j+c]>curr_len+1)):
                            helper(i+r,j+c,curr_len)
            return
        
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    helper(i,j,0)
        
        return
                