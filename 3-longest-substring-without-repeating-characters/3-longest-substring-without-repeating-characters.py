class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        cnt=0
        mx_cnt=0
        i=0
        j=0
        while j<len(s):
            if s[j] not in cache.keys():
                cache[s[j]]=1
                cnt+=1
                j+=1
            else:
                mx_cnt=max(cnt,mx_cnt)
                cnt=0
                cache={}
                i+=1
                j=i
        mx_cnt=max(cnt,mx_cnt)
        
        return mx_cnt