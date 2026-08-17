class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = dp[0]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]




        # def f(n):
        #     if n == 0:
        #         return 1
        #     if dp[n] != -1:
        #         return dp[n]
        #     L = f(n-1)
        #     if n<2:
        #         R = 0
        #     else:
        #         R = f(n-2)
        #     dp[n] = L+R
        #     return dp[n]
        
        
        # return f(n)    
        