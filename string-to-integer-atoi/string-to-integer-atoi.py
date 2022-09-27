class Solution:
    def myAtoi(self, s: str) -> int:
        flag_num=False
        flag_minus=False
        mn=-1*pow(2,31)
        mx=pow(2,31)-1
        ch_res=''
        s=s.strip()
        if len(s)==0:
            return 0
        if s[0]=='-':
            flag_minus=True
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        for i in s:
            if '0'<=i<='9':
                ch_res+=i
                flag_num=True
            else:
                break
        if len(ch_res)==0:
            return 0
        res=int(ch_res)
        if flag_minus:
            res*=-1
        if mn<=res<=mx:
            return res
        else:
            if res>mx:
                return mx
            else:
                return mn
        