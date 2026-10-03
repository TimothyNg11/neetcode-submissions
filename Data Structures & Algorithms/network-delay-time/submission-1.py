class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        seen = set()
        adjList = {i: [] for i in range(1, n+1)}
        for t in times:
            pre, post, time = t[0], t[1], t[2]
            adjList[pre].append((post, time))
        
        heapq.heappush(heap, (0, k))
        res = float('-inf')
        while heap:
            curr, node = heapq.heappop(heap)
            if node in seen:
                continue
            res = max(res, curr)
            seen.add(node)
            for post, time in adjList[node]:
                if post not in seen:
                    heapq.heappush(heap, (curr + time, post))
        
        if len(seen) == n:
            return res
        else:
            return -1


         

        