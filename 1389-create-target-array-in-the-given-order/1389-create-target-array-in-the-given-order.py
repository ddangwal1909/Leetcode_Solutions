class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res=[]
        for i in range(len(index)):
            if len(res)==0:
                res.append(nums[i])
            else:
                f_h = res[:index[i]]
                l_h = res[index[i]:]
                res=f_h
                res.append(nums[i])
                res.extend(l_h)
        return res
            