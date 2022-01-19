class Solution:
    def numTeams(self, rating: List[int]) -> int:
         
        pairs=0
        for i in range(1,len(rating)-1):
            gt_lt,gt_rt,ls_lt,ls_rt=0,0,0,0
            
            for j in range(0,i):
                if rating[j]<rating[i]:
                    ls_lt+=1
                else:
                    gt_lt+=1
            
            
            for j in range(i+1,len(rating)):
                if rating[j]<rating[i]:
                    ls_rt+=1
                else:
                    gt_rt+=1
            
            pairs+=((ls_lt*gt_rt)+(ls_rt*gt_lt))
            
        return pairs
            
                    
            
            