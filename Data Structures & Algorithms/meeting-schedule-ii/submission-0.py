"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #we need to track every meeting that hasnt ended by the next starting time
        intervals.sort(key=lambda x: x.start)
        endTimes = []

        for interval in intervals:
            if endTimes and endTimes[0] <= interval.start:
                heapq.heappop(endTimes)
            heapq.heappush(endTimes, interval.end)

        return len(endTimes)