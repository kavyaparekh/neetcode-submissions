class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        subset = []
        def bt(i, subset, tSum):
            if i>= len(nums) or tSum > target:
                return
            if tSum == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            tSum += nums[i]
            bt(i, subset, tSum)
            subset.pop()
            tSum -= nums[i]
            bt(i+1, subset, tSum)
        
        bt(0, [], 0)
        return res