class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = deque(), deque()
        pseen, aseen = set(), set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pac.append((i, j))
                    pseen.add((i, j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    atl.append((i, j))
                    aseen.add((i, j))
        
        # bfs from pacific
        while pac:
            x, y = pac.popleft()
            for nx, ny in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                rx, ry = x + nx, y + ny
                if rx >= 0 and ry >= 0 and rx < len(heights) and ry < len(heights[0]):
                    if (rx, ry) not in pseen and heights[rx][ry] >= heights[x][y]:
                        pseen.add((rx, ry))
                        pac.append((rx, ry))
        
        # bfs from pacific
        while atl:
            x, y = atl.popleft()
            for nx, ny in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                rx, ry = x + nx, y + ny
                if rx >= 0 and ry >= 0 and rx < len(heights) and ry < len(heights[0]):
                    if (rx, ry) not in aseen and heights[rx][ry] >= heights[x][y]:
                        aseen.add((rx, ry))
                        atl.append((rx, ry))
        res = []
        for a in range(len(heights)):
            for b in range(len(heights[0])):
                if (a, b) in aseen and (a, b) in pseen:
                    res.append([a, b])
        
        return res
        


        
            

            
            

        