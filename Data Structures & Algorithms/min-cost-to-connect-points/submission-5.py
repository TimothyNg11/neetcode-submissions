class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (dist, i, j))
        
        parent = {i: i for i in range(len(points))}     # every item is its own parent

        def find(x):
            while parent[x] != x:             # x isn't the root yet
                parent[x] = parent[parent[x]] # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False                  # already in the same group
            parent[ra] = rb                   # attach a's root under b's root
            return True

        cost = 0
        counter = 0
        while heap:
            dist, i, j = heapq.heappop(heap)
            if counter == len(points) - 1:
                return cost
            if union(i, j):
                cost += dist
                counter += 1
        
        return cost


        