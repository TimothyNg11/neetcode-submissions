class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}
        for flight in flights:
            start, end, price = flight[0], flight[1], flight[2]
            adjList[start].append((end, price))
        
        heap = []
        heapq.heappush(heap, (0, src, k))
        seen = set()
        while heap:
            dist, start, stops = heapq.heappop(heap)
            if (start, stops) in seen:
                continue
            if stops <= -1:
                continue
            if start == dst:
                return dist
            seen.add((start, stops))
            for child in adjList[start]:
                end, price = child[0], child[1]
                if (end, stops) not in seen:
                    if end != dst:
                        heapq.heappush(heap, (dist + price, end, stops - 1))
                    else:
                        heapq.heappush(heap, (dist + price, end, stops))
        
        return -1
        

            
        