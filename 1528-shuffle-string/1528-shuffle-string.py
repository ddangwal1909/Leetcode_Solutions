class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_res=''
        for i in range(len(indices)):
            str_res+=s[indices.index(i)]
        return str_res