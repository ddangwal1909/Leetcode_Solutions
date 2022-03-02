class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [ amount+1 for i in range(amount+1)]
        self.amount = amount
        self.recursion(coins, amount)
        if self.dp[amount] == self.amount+1:
            return -1
        else:
            return self.dp[amount]
    def recursion(self,coins,amount):
        
        if amount == 0:
            self.dp[0]=0
            return 0
        if amount<min(coins):
            return -1
        if self.dp[amount] !=  self.amount+1:
            return self.dp[amount]
        
        for coin in coins:
            if coin>amount:
                continue
            if self.dp[amount-coin] != self.amount+1:
                sub_problem = self.dp[amount-coin]
            else:
                sub_problem = self.recursion(coins,amount-coin)
            if sub_problem + 1 < self.dp[amount] and sub_problem >= 0:
                self.dp[amount] = sub_problem + 1

        if self.dp[amount] !=  self.amount+1:
            return self.dp[amount]
        else:
            self.dp[amount] = -1
            return -1