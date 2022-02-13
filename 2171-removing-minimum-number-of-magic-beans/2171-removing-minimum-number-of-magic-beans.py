class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        mn=math.inf
        n=len(beans)
        sm=sum(beans)
        for i in range(len(beans)):
            curr_steps=(sm-(n-i)*beans[i]) 
            #hashmap[beans[i]]=curr_steps
            mn=min(curr_steps,mn)
            #print(beans[i],curr_steps)
        return mn
            