class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        mem = [[-1 for _ in range(m)] for _ in range(n)]
        
        def recursive(i1, i2):
            if i1 >= n or i2 >= m: return 0
            if mem[i1][i2] != -1: return mem[i1][i2]
            
            case1 = case2 = case3 = 0
            
            if s1[i1] == s2[i2]:
                case1 = 1 + recursive(i1+1, i2+1)
            
            case2 = recursive(i1+1, i2)
            case3 = recursive(i1, i2+1)
            mem[i1][i2] = max(case1, case2, case3)
            
            return mem[i1][i2]
            
        return recursive(0, 0)