class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        lst=list(s)
        stck=[]
        remove=[]
        
        for i in range(len(lst)):
            if lst[i] == '(':
                stck.append((i,lst[i]))
            elif lst[i]==')':
                if stck:
                    if stck[-1][1]=='(':
                        stck.pop()
                else:
                    remove.append(i)
            else:
                continue
        
        for i in stck:
            remove.append(i[0])
        
        res=''
        
        for j in range(len(lst)):
            if j not in remove:
                res+=lst[j]
        
        return res