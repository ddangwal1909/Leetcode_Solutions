class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptr1,ptr2=0,0
        
        s1=''
        t1=''
        for i in range(len(s)):
            if i==0 and s[i]=='#':
                continue
            elif s[i]=='#':
                s1=s1[:-1]
            else:
                s1+=s[i]
        
        
        for i in range(len(t)):
            if i==0 and t[i]=='#':
                continue
            elif t[i]=='#':
                t1=t1[:-1]
            else:
                t1+=t[i]
        
        return s1==t1
        