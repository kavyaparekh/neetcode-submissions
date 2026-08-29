class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= []
        for i in range(m):
            dp.append([-1]*n)

        def f(r,c):
            if r==0 and c==0:
                return 1
            if r<0 or c<0:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            left = f(r,c-1)
            top = f(r-1,c)

            dp[r][c] = left+top
            return dp[r][c]
        
        return f(m-1, n-1)