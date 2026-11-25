class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ls = []
        if key in self.mp.keys():
            ls.extend(self.mp[key])
        
        l = 0
        r = len(ls)-1
        res = ""
        while l<=r:
            mid = l + (r-l)//2
            if ls[mid][1] == timestamp:
                return ls[mid][0]
            elif ls[mid][1] <= timestamp:
                res = ls[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
        
