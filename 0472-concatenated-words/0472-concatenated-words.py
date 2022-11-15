class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        set_w=set(words)
        def helper(w):
            if w in hashtable:
                return hashtable[w]
            hashtable[w]=False
            for i in range(1,len(w)):
                p=w[:i]
                s=w[i:]
                if p in set_w and s in set_w:
                    hashtable[w]=True
                    return True
                if p in set_w and helper(s):
                    hashtable[w]=True
                    return True
                if helper(p) and s in set_w:
                    hashtable[w]=True
                    return True
            return False
        hashtable={}
        res=[]
        for i in words:
            if helper(i)==True:
                res.append(i)
        
        return res