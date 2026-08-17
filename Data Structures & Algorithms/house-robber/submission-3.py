class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        if n==1:
            return dp[0]
            
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            pick = nums[i] + dp[i-2]
            notpick = 0 + dp[i-1]
            
            dp[i] = max(pick,notpick)
        
        return dp[n-1]



        # def f(i):
        #     if i == 0:
        #         return nums[i]
        #     if i<0:
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     pick = nums[i] + f(i-2)
        #     notpick = 0 + f(i-1)
        #     dp[i] = max(pick, notpick)

        #     return dp[i]
        
        return f(n-1)