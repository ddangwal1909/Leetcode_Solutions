class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp=1
        while tmp<=n:
            if tmp==n:
                return True
            else:
                tmp=(tmp<<1)
                print(tmp)
        return False
        