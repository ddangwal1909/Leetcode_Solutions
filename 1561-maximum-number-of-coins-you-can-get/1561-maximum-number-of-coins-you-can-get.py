class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        k_start = int(len(piles)/3)
        
        piles_new=piles[k_start:]
        
        res= sum(piles_new[::2])
        
        return res