class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]-mn>profit:
                profit=prices[i]-mn
            else:
                mn=min(mn,prices[i])
        
        return profit