class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod = 1
        postfixprod = 1
        prefixres = []
        postfixres = []
        res = []
        for i in range(len(nums)):
            prefixprod*=nums[i]
            prefixres.append(prefixprod)
      
        
        for i in range(len(nums)-1, -1, -1):
            postfixprod*=nums[i]
            postfixres.append(postfixprod)
        postfixres.reverse()

        for i in range(len(nums)):
            if i-1<0:
                val1 = 1
            else:
                val1 = prefixres[i-1]
            
            if i+1>=len(nums):
                val2 = 1
            else:
                val2 = postfixres[i+1]
            res.append(val1*val2)

        return res

        # ls = [1,5,7,4,2]
        # print(ls[-1])

        