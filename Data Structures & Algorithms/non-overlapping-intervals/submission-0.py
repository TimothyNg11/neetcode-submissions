class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = float('-inf')
        total = 0
        for interval in intervals:
            start, end = interval[0], interval[1]
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                total += 1
        
        return total
            
        