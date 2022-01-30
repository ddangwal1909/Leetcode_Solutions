class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ending_time = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            next_start_time = intervals[i][0]
            next_end_time = intervals[i][1]
            
            if next_start_time >=ending_time:
                ending_time = next_end_time
            else:
                count += 1
                
        return count
            
                