class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        res=[]
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res