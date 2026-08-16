class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def targetSum(i, subset, tSum):
            if i >= len(nums) or tSum > target:
                return
            if tSum== target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            tSum += nums[i]
            targetSum(i, subset, tSum)
            subset.pop()
            tSum -= nums[i]
            targetSum(i+1, subset, tSum)

        targetSum(0,[], 0)
        return res