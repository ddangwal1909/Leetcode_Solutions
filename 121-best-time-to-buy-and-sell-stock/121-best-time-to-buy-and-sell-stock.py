class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit_max=0
        lower=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<lower:
                lower=prices[i]
            else:
                if prices[i]-lower>profit_max:
                    profit_max=prices[i]-lower
        
        return profit_max
            