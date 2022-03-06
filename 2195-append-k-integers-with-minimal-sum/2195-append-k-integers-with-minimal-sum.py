class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        res = 0
        nums.insert(0, 0)
        nums.append(2000000001)
        n = len(nums)
        for i in range(n-1):
            s=nums[i]
            e=nums[i+1]
            if s==e:
                continue
            n = min(e-s-1,k)
            res+= (n*(2*(s+1)+(n-1))//2)
            k-=n
            if k==0:
                break
        return res