class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def dfs(i: int) -> (int, int):
            if table[i] != (-1, -1):
                return table[i]
            
            maxLen, maxCount = 1, 0
            
            for j in range(i + 1, n):
                
                if nums[i] < nums[j]:
                    
                    nextLen, nextCount = dfs(j)
                    
                    if maxLen == nextLen + 1:
                        maxCount += nextCount
                    elif maxLen < nextLen + 1:
                        maxLen = nextLen + 1
                        maxCount = nextCount
                        
            maxCount = max(1, maxCount)
            table[i] = (maxLen, maxCount)
            return table[i]
        
        n = len(nums)
        table = [(-1, -1)] * n
        maxLen, maxCount = 0, 0
        
        for i in range(n):
            currLen, currCount = dfs(i)
            
            if currLen == maxLen:
                maxCount += currCount
            elif currLen > maxLen:
                maxLen = currLen
                maxCount = currCount
            
        return maxCount