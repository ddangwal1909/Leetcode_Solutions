class Solution:
    
    def getord(self,ch):
        return ord(ch)-ord('1')+1
    
    def getchar(self,num):
        return chr(ord('1')+num-1)
    
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        i=len(num1)-1
        j=len(num2)-1
        res=''
        while i>=0 and j>=0:
            tmp=self.getord(num1[i])+self.getord(num2[j])
            curr=(tmp+carry)%10
            carry=(tmp+carry)//10
            res+=self.getchar(curr)
            i-=1
            j-=1
            print(carry)
        
        print(i,j)
        print(res[::-1])
        print(carry)
        if i>=0:
            while i>=0:
                tmp=self.getord(num1[i])
                curr=(tmp+carry)%10
                carry=(tmp+carry)//10
                res+=self.getchar(curr)
                i-=1
                print(res[::-1])
        if j>=0:
            while j>=0:
                tmp=self.getord(num2[j])
                curr=(tmp+carry)%10
                carry=(tmp+carry)//10
                res+=self.getchar(curr)
                j-=1
                print(res[::-1])
        print(carry)
        print(res[::-1])
        if carry!=0:
            res+=self.getchar(carry)
        print(res[::-1])
        res_final=res[::-1]
        return res_final
                
            
            
        