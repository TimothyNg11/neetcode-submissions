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
        prev = float('-inf')
        earliest_end = []
        rooms = 1
        for interval in intervals:
            start, end = interval.start, interval.end
            if not earliest_end:
                heapq.heappush(earliest_end, end)
            elif start >= earliest_end[0]:
                heapq.heappop(earliest_end)
                heapq.heappush(earliest_end, end)
            elif start < prev:
                rooms += 1
                heapq.heappush(earliest_end, end)
            prev = end
        
        return 0 if not intervals else rooms
            
        