class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        initial=strs[0]
        if len(initial)==0:
            return ""
        
        for i in strs[1:]:
            j=0
            while j<len(i) and j<len(initial):
                if i[j]==initial[j]:
                    j+=1
                else:
                    break
            initial=initial[:j]
            if len(initial)==0:
                break
        
        return initial