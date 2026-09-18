class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        seen = [0 for i in range(n)]

        for edge in edges:
            a, b = edge[0], edge[1]
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(node):
            if seen[node]:
                return

            seen[node] = 1
            for c in adjList[node]:
                dfs(c)
        
        count = 0
        for i in range(n):
            if not seen[i]:
                dfs(i)
                count += 1
        
        return count
        