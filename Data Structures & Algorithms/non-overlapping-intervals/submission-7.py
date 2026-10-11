class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s < prev_end:
                res += 1
                prev_end = min(prev_end, e)
            else:
                prev_end = e
        return res