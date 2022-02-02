class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst_arr=list(s.split())
        hashtable={}
        hashtable2={}
        if len(lst_arr)!=len(pattern):
            return False
        
        for i in range(len(lst_arr)):
            if pattern[i] not in hashtable.keys() and lst_arr[i] not in hashtable2.keys():
                hashtable[pattern[i]]=lst_arr[i]
                hashtable2[lst_arr[i]]=pattern[i]
            elif (pattern[i] in hashtable.keys() and lst_arr[i] not in hashtable2.keys()) or ((pattern[i] not in hashtable.keys() and lst_arr[i] in hashtable2.keys())):
                return False
                
            else:
                if hashtable[pattern[i]] != lst_arr[i] or hashtable2[lst_arr[i]]!=pattern[i]:
                    return False
        return True
        