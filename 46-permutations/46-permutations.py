class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        
        def helper(k_tmp,curr):
            
            if k_tmp==0:
                output.append(curr[:])
                return
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    helper(k_tmp-1,curr)
                    curr.pop()
            
        
        helper(len(nums),[])
        
        return output
                    
            
        