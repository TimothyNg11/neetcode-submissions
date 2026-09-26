class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}
        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            if i+1 < len(s) and s[i:i+2] in {str(i) for i in range(10, 27)}:
                res = dfs(i+1) + dfs(i+2)
            else:
                res = dfs(i+1)
            memo[i] = res
            return res
        
        return dfs(0)
