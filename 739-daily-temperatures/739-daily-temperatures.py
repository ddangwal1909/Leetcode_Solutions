class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stck=[(temperatures[-1],len(temperatures)-1)]
        res=[0]*len(temperatures)
        
        for i in range(len(temperatures)-2,-1,-1):
            
            while stck and stck[-1][0]<=temperatures[i]:
                stck.pop()
            
            if stck:
                res[i]=stck[-1][1]-i
            
            stck.append((temperatures[i],i))
            #print(stck)
        return res
                