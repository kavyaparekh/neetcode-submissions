class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        farthest = 0
        currEnd = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == currEnd:
                jump += 1
                currEnd = farthest
        return jump
        