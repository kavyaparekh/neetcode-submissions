class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(lambda: [-1,-1])
        res = []
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]][0] = i
            else:
                d[s[i]][1] = i
        for key, val in d.items():
            if val[1] == -1:
                val[1] = val[0]
            if res and val[0] < res[-1][1]:
                #res[-1][0] = min(res[-1][0], val[0])
                res[-1][1] = max(res[-1][1], val[1])
            else:
                res.append(val)
                
        return  [(end-start+1) for start, end in res]     


