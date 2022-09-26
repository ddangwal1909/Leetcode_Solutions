class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        j=len(digits)-1
        
        while j>=0:
            if digits[j]+carry>9:
                carry_tmp=int((digits[j]+carry)/10)
                digits[j]=(digits[j]+carry)%10
                carry=carry_tmp
                if carry==0:
                    break
            else:
                digits[j]+=carry
                carry=0
                break
                
            j-=1
        
        if carry!=0:
            digits.insert(0,carry)
        return digits