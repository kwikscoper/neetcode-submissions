"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        inProgress = []
        maxRooms = 0

        for interval in intervals:
            while inProgress and inProgress[0] <= interval.start:
                heapq.heappop(inProgress)
            heapq.heappush(inProgress, interval.end)
            maxRooms = max(maxRooms, len(inProgress))

        return maxRooms