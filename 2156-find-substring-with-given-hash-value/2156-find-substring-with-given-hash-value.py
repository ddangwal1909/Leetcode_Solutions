class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(ch):
            return ord(ch) - ord('a') + 1
        
        def build_res(start,):
            res = []
            for i in range(start, start + k):
                res.append(s[i])
            return "".join(res)
                

        curr_hash = 0
        p = 1
        for i in range(k):
            curr_hash += (val(s[i]) * p)
            p *= power

            
        b, pk = 0, pow(power, k)
        for i in range(k, len(s)):
            if curr_hash % modulo == hashValue:
                return build_res(b)
            
            curr_hash -= (val(s[b]))
            curr_hash += (val(s[i]) * pk)
            curr_hash //= power # remove a multiple of power
            b += 1
        
        return build_res(b)