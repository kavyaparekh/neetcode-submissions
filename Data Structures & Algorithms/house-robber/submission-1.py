class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        def f(i):
            if i == 0:
                return nums[i]
            if i<0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            pick = nums[i] + f(i-2)
            notpick = 0 + f(i-1)
            dp[i] = max(pick, notpick)

            return dp[i]
        
        return f(n-1)