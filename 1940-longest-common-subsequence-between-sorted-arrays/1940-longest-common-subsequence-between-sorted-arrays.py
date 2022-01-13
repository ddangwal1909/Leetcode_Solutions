class Solution:
    def common_twoarrays(self,arr1,arr2):
        
        i,j=0,0
        res=[]
        while i<len(arr1) and j<len(arr2):
            if arr1[i]==arr2[j]:
                res.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
        
        return res
            
            
        
    
    
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        arr1=arrays[0]
        arr2=arrays[1]
        res=self.common_twoarrays(arr1,arr2)
        for i in range(2,len(arrays)):
            res=self.common_twoarrays(arrays[i],res)
        
        return res
            