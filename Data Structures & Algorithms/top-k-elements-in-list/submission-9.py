class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        max_freq = float('-inf')
        for val in count.values():
            max_freq = max(max_freq, val)
        
        arr = [[] for i in range(max_freq+1)]
        for key, value in count.items():
            arr[value].append(key)
        
        res = []
        while len(res)<k:
            temp = arr.pop()
            for element in temp:
                if len(res)<k:
                    res.append(element)
        
        return res




        
        


