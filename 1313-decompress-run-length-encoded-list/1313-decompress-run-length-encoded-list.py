class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=1
        res=[]
        while(i<len(nums)):
            for j in range(nums[i-1]):
                res.append(nums[i])
            i+=2
        return res