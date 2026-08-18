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
            r = float('inf')
            for c in coins:
                r = min(r, f(amount-c))
            dp[amount] = 1+r
            return dp[amount]

        result = f(amount)  

        return result if result != float('inf') else -1