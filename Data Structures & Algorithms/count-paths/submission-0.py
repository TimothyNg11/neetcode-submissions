class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n = m - 1 + n - 1
        return math.comb(n, m-1)
        