class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"

                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    total = total + 1
                    dfs(i, j)
            
        return total