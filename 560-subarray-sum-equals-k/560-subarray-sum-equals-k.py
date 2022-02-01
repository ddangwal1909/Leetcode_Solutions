class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict_map={}
        sm=0
        dict_map[0]=1
        cnt=0
        for i in range(len(nums)):
            sm+=nums[i]
            if sm-k in dict_map.keys():
                cnt+=dict_map[sm-k]
            if sm not in dict_map.keys():
                dict_map[sm]=1
            else:
                dict_map[sm]+=1
        return cnt
        
        