class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def targetSum(i, subset, tSum):
            
            if tSum == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or tSum > target:
                return

            subset.append(candidates[i])
         
            targetSum(i+1, subset, tSum + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            targetSum(i+1, subset, tSum)

        targetSum(0, [], 0)
        return res