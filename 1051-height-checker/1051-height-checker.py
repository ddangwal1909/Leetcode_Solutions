class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_arr=sorted(heights)
        res=0
        for i in range(len(new_arr)):
            if new_arr[i]!=heights[i]:
                res+=1
        
        return res
        