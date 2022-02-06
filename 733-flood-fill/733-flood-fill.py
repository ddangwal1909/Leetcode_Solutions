class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldcolor=image[sr][sc]
        
        visited=[]
        def helper(i,j):
            image[i][j]=newColor
            for r,c in [(0,1),(1,0),(0,-1),(-1,0)]:
                if (i+r)<len(image) and (j+c)<len(image[0]) and (i+r)>=0 and (j+c)>=0:
                    if image[i+r][j+c]==oldcolor:
                        if (i+r,j+c) not in visited:
                            visited.append((i+r,j+c))
                            helper(i+r,j+c)
        
        helper(sr,sc)
        
        return image