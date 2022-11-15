class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        res=0
        def helper(nums):
            nonlocal res
            if len(nums)==1:
                res=nums[0]
                return
            else:
                nxt_arr=[]
                for i in range(0,len(nums)-1):
                    nxt_arr.append((nums[i]+nums[i+1])%10)
                helper(nxt_arr)
        
        helper(nums)
        return res