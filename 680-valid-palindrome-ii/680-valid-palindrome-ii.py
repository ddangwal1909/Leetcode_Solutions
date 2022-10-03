class Solution:
    
    def checkpalin(self,i,j,s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        flag=False
        while i<=j:
            if s[i]!=s[j]:
                return self.checkpalin(i+1,j,s) or self.checkpalin(i,j-1,s) 
            i+=1
            j-=1
        return True