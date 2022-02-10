class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}

        def helper(s,hashtable,start):
            nonlocal memo
            if start in memo.keys():
                return memo[start]
            
            elif len(s)==start:
                return True
            else:
                for end in range(start+1,len(s)+1):
                    #print(s[start:end])
                    if (s[start:end] in hashtable):
                        if helper(s,hashtable,end):
                            memo[start]=True
                            return True
                memo[start]=False
                return False
        
        return helper(s,set(wordDict),0)  
        
        