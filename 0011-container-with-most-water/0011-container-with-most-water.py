class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i=0
        j=len(height)-1
        mx_a=0
        while i<j:
            mx_a=max(min(height[i],height[j])*(j-i),mx_a)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        
        return mx_a