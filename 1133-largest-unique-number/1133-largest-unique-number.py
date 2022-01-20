class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        lst=[]
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq.keys():
                freq[nums[i]]=1
                lst.append(nums[i])
            else:
                freq[nums[i]]+=1
        
        lst.sort()
        j=len(lst)-1
        while j>=0:
            if freq[lst[j]]==1:
                res=lst[j]
                break
            j-=1
        if j==-1:
            return -1
        else:
            return res