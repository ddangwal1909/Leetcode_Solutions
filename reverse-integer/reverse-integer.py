class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if x<0:
            flag=1
        x=abs(x)
        chr=str(x)
        chr=chr[::-1]
        x=int(chr)
        if flag==1:
            x*=-1
        if x>=-1*(pow(2,31)) and x<=pow(2,31)-1:
            return x
        else:
            return 0
        