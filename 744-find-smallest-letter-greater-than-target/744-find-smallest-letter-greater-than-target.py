class Solution:
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start,end=0,len(letters)
        
        if target<letters[0]:
            return letters[0]
        
        if target>=letters[-1]:
            return letters[0]
        
        while start<end:
            
            md=(start+end)//2
            
            if letters[md]>target and letters[md-1]<=target:
                return letters[md]
            elif letters[md]>target:
                end=md
            else:
                start=md+1
        
        return -1
            
        
        