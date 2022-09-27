class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            dict={}
            for i in s:
                if i not in dict.keys():
                    dict[i]=1
                else:
                    dict[i]+=1
            flag=True
            for i in t:
                if i not in dict.keys():
                    flag=False
                    break
                else:
                    if dict[i]==0:
                        flag=False
                        break
                    else:
                        dict[i]-=1
            return flag