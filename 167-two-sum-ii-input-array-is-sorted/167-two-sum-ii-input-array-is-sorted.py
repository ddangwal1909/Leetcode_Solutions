class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i,j=0,len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                res=[i+1,j+1]
                break
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        
        return res
        