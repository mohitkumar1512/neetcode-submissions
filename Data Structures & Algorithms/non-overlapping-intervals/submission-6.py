class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        prev = intervals[0]
        res = 0
        for s, e in intervals[1:]:
            if prev[1] > s:
                res += 1
            else:
                prev = [s, e]
        return res