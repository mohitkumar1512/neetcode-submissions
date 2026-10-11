"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals:
            intervals.sort(key=lambda x: x.start)
            prev_end = intervals[0].end
            for inter in intervals[1:]:
                if inter.start >= prev_end:
                    prev_end = max(prev_end, inter.end)
                else:
                    return False
        return True