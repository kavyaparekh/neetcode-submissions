class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            res = []
            for coin in coins:
                if i-coin < 0:
                    val = float('inf')
                else:
                    val = dp[i-coin]
                res.append(val)
            dp[i] = 1 + min(res)
        
        return dp[amount] if dp[amount] < float('inf') else -1
