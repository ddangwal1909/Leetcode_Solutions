class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        result=[]
        stack=[]
        for i in prices[::-1]:
            
            while stack and stack[-1]>i:
                stack.pop()
                
            if stack and stack[-1]<=i:
                result.append(abs(stack[-1]-i))
            else:
                result.append(i)
            
            stack.append(i)
        
        result=result[::-1]
        return result