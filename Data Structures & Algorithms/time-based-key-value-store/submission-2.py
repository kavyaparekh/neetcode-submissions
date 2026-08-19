class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)      

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp[key]
        l = 0
        r = len(arr)-1
        res = ""

        while l<=r:
            mid = l +(r-l)//2
            
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
                


        
