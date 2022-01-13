class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        mx=-1000
        nums.sort()
        while(i<j):
            mx=max(mx,nums[i]+nums[j])
            i+=1
            j-=1
            
        return mx