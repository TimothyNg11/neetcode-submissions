import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        self.counter = 0
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)  
        val = -heapq.heappop(self.small)
        heapq.heappush(self.big, val)
        if len(self.big) > len(self.small):
            a = heapq.heappop(self.big)
            heapq.heappush(self.small, -a)

    def findMedian(self) -> float:
        length = len(self.small) + len(self.big)
        if length % 2:
            return float(-self.small[0])
        return (-self.small[0] + self.big[0]) / 2
    
        