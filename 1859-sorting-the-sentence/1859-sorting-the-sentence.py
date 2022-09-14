class Solution:
    def sortSentence(self, s: str) -> str:
        
        lst=[None for i in range(9)]
        
        for i in s.split():
            idx=ord(i[-1])-ord('0')-1
            lst[idx]=i[:-1]
        
        res=''
        for j in lst:
            if j is None:
                break
            else:
                res+=j
                res+=' '
        return res[:-1]