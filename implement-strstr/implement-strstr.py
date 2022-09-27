class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        while j<len(haystack):
            if haystack[j]==needle[0]:
                if j+len(needle)<=len(haystack):
                    if haystack[j:j+len(needle)]==needle:
                        return j
            j+=1
        return -1
                    
                
        