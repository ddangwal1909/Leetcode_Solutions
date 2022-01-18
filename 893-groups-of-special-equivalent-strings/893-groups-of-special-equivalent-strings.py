class Solution:
    
    def getlsts(self,word):
        odd=[]
        even=[]
        for i in range(len(word)):
            if i%2==0:
                even.append(word[i])
            else:
                odd.append(word[i])
        odd.sort()
        even.sort()
        return (odd,even)
    
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        even=[]
        odd=[]
        visited=[False for i in range(len(words))]
        i=0
        res=0
        while i<len(words):
            if visited[i]==True:
                i+=1
            else:
                visited[i]==True
                res+=1
                odd_orig,even_orig=self.getlsts(words[i])
                for j in range(i+1,len(words)):
                    if visited[j]==False:
                        odd_curr,even_curr=self.getlsts(words[j])
                        if odd_curr==odd_orig and even_orig==even_curr:
                            visited[j]=True
                        else:
                             continue
                i+=1
        
        return res
                
            
        
        