import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        
    def findMedian(self) -> float:
        copy = self.heap.copy()
        length = len(copy)
        if length % 2 != 0:
            for i in range(length // 2):
                heapq.heappop(copy)
            return float(heapq.heappop(copy))
        else:
            for j in range(int(length / 2 - 1)):
                heapq.heappop(copy)
            median = (heapq.heappop(copy) + heapq.heappop(copy)) / 2
            return float(median)
        