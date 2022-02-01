class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap={}
        for i in s:
            if i not in hashmap.keys():
                hashmap[i]=1
            else:
                hashmap[i]+=1
        max_pal=0
        cnt=0
        for j in hashmap.keys():
            if hashmap[j]%2==1:
                cnt=1
            max_pal+=((hashmap[j]//2)*2)
        
        max_pal+=cnt
        
        return max_pal
                