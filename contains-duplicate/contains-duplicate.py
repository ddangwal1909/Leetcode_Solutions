class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary={}
        dictionary={i:1 for i in nums if i not in dictionary.keys()}
        print(dictionary)
        if len(dictionary.keys())==len(nums):
            return False
        else:
            return True
        