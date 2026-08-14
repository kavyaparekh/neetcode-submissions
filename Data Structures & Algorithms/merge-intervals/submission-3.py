class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
       
        intervals.sort()
        res.append(intervals[0])
        
        i = 1
        while i<len(intervals):
            if intervals[i][0] <= res[-1][1]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
            i+=1
        return res
            
            


        