class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        minnum = 0
        while queue:
            x, y, count = queue.popleft()
            minnum = max(minnum, count)
            for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rx, ry = x + nx, y + ny
                if rx >= 0 and ry >= 0 and rx < len(grid) and ry < len(grid[0]) and grid[rx][ry] == 1:
                    grid[rx][ry] = 2
                    queue.append((rx, ry, count + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return minnum
        
                    
            


                