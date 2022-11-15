class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lft=[]
        rgt=[]
        p=[]
        for i in nums:
            if i==pivot:
                p.append(pivot)
            elif i<pivot:
                lft.append(i)
            else:
                rgt.append(i)
        
        res=[]
        res.extend(lft)
        res.extend(p)
        res.extend(rgt)
        return res
        
                