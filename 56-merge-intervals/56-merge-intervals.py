class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        curr_start=intervals[0][0]
        curr_end=intervals[0][1]
        
        
        i=1
        
        res=[]
        
        
        while i<len(intervals):
            if curr_end<intervals[i][0] or curr_start>intervals[i][1]:
                res.append([curr_start,curr_end])
                curr_start=intervals[i][0]
                curr_end=intervals[i][1]
            else:
                curr_start=min(intervals[i][0],curr_start)
                curr_end=max(intervals[i][1],curr_end)
            i+=1
        res.append([curr_start,curr_end])
        return res
            
        