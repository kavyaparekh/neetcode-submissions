class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1]*(amount+1)
        def f(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            

            if dp[amount] != -1:
                return dp[amount]

            res = []
            for coin in coins:
                res.append(1+f(amount-coin))
            
            dp[amount] = min(res)
            return dp[amount]

        minCoins = f(amount)

        return -1 if minCoins >= float('inf') else minCoins

