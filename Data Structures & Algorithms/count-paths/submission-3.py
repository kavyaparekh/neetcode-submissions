class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= []
        for i in range(m):
            dp.append([-1]*n)
        
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r==0 and c==0:
                    continue
                if c-1<0:
                    left = 0
                else: 
                    left = dp[r][c-1]
                if r-1<0:
                    top= 0
                else:
                    top = dp[r-1][c]
                dp[r][c] = left+top
        
        return dp[m-1][n-1]


        

        # def f(r,c):
        #     if r==0 and c==0:
        #         return 1
        #     if r<0 or c<0:
        #         return 0

        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     left = f(r,c-1)
        #     top = f(r-1,c)

        #     dp[r][c] = left+top
        #     return dp[r][c]
        
        # res = f(m-1, n-1)
        # return res
        