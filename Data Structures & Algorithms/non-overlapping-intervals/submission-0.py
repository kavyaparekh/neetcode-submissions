class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
                i+=1
            else:
                count += 1
                prevEnd = min(intervals[i][1], prevEnd)
                i+=1
        return count

            