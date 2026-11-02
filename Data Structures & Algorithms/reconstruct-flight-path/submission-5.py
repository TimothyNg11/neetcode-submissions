class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):  # reverse so pop() gives smallest
            adj[a].append(b)
        res = []

        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())   # use the ticket for good, no undo
            res.append(node)           # add only once node is stuck

        dfs('JFK')
        return res[::-1]