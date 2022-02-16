class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i,j=0,len(height)-1
        mx=0
        while i<j:
            
            h=min(height[i],height[j])
            w=j-i
            
            mx = max(mx,w*h)
                
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        
        return mx