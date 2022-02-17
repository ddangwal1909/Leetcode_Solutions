class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        
        prod_so_far=1
        res=0
        l=0
        r=0
        
        if k==0:
            return 0
        
        while r<len(nums):
            prod_so_far=prod_so_far*nums[r]
            #print(prod_so_far,r,l,res)
            if prod_so_far<k:
                res+=(r-l+1)
            else:
                while prod_so_far>=k and l<=r:
                    prod_so_far//=nums[l]
                    l+=1
                res+=(r-l+1)
            r+=1
        
        return res
        