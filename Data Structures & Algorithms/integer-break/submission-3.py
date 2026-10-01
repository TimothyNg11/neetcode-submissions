class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 0:
                return 1
            if i in memo:
                return memo[i]
            
            arr = []
            for j in range(1, i // 2 + 2):
                arr.append(dfs(i-j) * j)
            
            if i != n:
                memo[i] = max(i, max(arr))
            else:
                memo[i] = max(arr)
            return memo[i]
        if n == 2:
            return 1
        return dfs(n)
        