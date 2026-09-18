class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            
            seen.add(node)
            for c in adjList[node]:
                if c == parent:
                    continue
                else:
                    if not dfs(c, node):
                        return False
        
            return True

        return dfs(0, -67) and len(seen) == n
        