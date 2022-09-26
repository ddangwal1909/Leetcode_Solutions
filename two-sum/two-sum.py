class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        res=[]
        for i in range(len(nums)):
            if (target-nums[i]) in f.keys():
                res.append(f[target-nums[i]])
                res.append(i)
                break
            if nums[i] not in f.keys():
                f[nums[i]]=i        
        return res
        