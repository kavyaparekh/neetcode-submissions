class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max