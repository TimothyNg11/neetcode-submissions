class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            
            if end < newInterval[0]:
                res.append(interval)
            elif start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif end >= newInterval[0]:
                a = min(start, newInterval[0])
                b = max(end, newInterval[1])
                newInterval = [a, b]
        
        if not res or res == intervals:
            res.append(newInterval)
        return res
        