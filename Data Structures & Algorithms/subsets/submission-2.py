class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def bt(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            bt(i+1, subset)
            subset.pop()
            bt(i+1, subset)
        
        bt(0, [])
        return res
