class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        hashtable = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        
        
        curr=[]
        for i in digits:
            a = curr
            b = hashtable[i]
            if len(curr)>0:
                curr=[]
                for k in a:
                    for l in b:
                        tmp = k+l
                        curr.append(tmp)
            else:
                curr = b
        
        return curr
                    
        