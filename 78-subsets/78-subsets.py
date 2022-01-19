class Solution:
    
    def givebinary(self,l,ln):
        binary=[]
        while l:
            if l%2==0:
                binary.append(0)
            else:
                binary.append(1)
            l=l//2
            
        if len(binary)!=ln:
            st=len(binary)
            en=ln
            #print(st,en)
            for i in range(st,en):
                binary.append(0)
        binary=binary[::-1]
        return binary
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        
        for i in range((2**(len(nums)))):
            tmp=[]
            s=self.givebinary(i,len(nums)) 
            print(s)
            for j in range(len(s)):
                if s[j] == 1:
                    tmp.append(nums[j])
                else:
                    continue
            
            res.append(tmp)
        
        return res
        