class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        change=target[0]
        for i in range(1,len(target)):
            change+=max(0,target[i]-target[i-1])
        
        return change
        