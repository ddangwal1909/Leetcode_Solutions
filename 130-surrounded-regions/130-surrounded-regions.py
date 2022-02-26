class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        mx_r = len(board)
        mx_c = len(board[0])
        
        
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        for i in range(mx_r):
            for j in range(mx_c):
                if board[i][j]=='X':
                    visited[i][j]=True
        
                    
        
        def dfs(i,j):
            
            visited[i][j]=True
            board[i][j]='S'
            for r,c in directions:
                if 0<=(i+r)<mx_r and 0<=(j+c)<mx_c and visited[i+r][j+c]==False and board[i+r][j+c]=='O':
                    dfs(i+r,j+c)
            return
        
        
        for i in range(mx_r):
            if board[i][0]=='O' and visited[i][0]==False:
                dfs(i,0)
        
        for i in range(mx_r):
            if board[i][mx_c-1]=='O' and visited[i][mx_c-1]==False:
                dfs(i,mx_c-1)
        
        
        for i in range(mx_c):
            if board[0][i]=='O' and visited[0][i]==False:
                dfs(0,i)
                
                
        for i in range(mx_c):
            if board[mx_r-1][i]=='O' and visited[mx_r-1][i]==False:
                dfs(mx_r-1,i)
        
        print(board)
        
        for i in range(mx_r):
            for j in range(mx_c):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'
        
        
        return
        
        
        
        
                
        
        
        
        
        
        
        
        