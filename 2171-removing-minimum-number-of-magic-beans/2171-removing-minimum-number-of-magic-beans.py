class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        mn=math.inf
        n=len(beans)
        sm=sum(beans)
        prefix=[0]*(len(beans)+1)
        prefix[0]=0
        for i in range(len(beans)):
            prefix[i+1]=prefix[i]+beans[i]
        #print(prefix)
        #hashmap={}
        
        for i in range(len(beans)):
            curr_steps=(sm-(n-i)*beans[i]) 
            #hashmap[beans[i]]=curr_steps
            mn=min(curr_steps,mn)
            #print(beans[i],curr_steps)
        return mn
            