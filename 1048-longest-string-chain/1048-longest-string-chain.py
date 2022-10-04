class Solution:
    def longestStrChain(self, words):
        dp = {}
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            dp[words[i]]=1
            for j in range(len(words[i])):
                if words[i][:j]+words[i][j+1:] in dp:
                    dp[words[i]]=max(dp[words[i][:j]+words[i][j+1:]]+1,dp[words[i]])
        print(dp)
        return max(dp.values())
        
            
            