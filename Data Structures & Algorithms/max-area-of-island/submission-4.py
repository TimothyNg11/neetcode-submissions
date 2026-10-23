class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        counter = 0
        def dfs(i, j):
            if i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 and grid[i][j] == 1:
                grid[i][j] = 0
                area = 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
                return area
            return 0

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    counter = max(counter, temp)
        return counter


        