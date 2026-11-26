class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        arr = []
        for key,val in count.items():
            arr.append((val,key))
        arr.sort()
        
        res = []
        while len(res)<k:
            val, key = arr.pop()
            res.append(key)
        
        return res
        


