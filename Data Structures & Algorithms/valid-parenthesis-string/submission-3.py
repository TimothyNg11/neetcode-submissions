class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dp(i, l, r):
            if r > l:
                return False
            if i == len(s):
                if l == r:
                    return True
                return False
            if (i, l, r) in memo:
                return memo[(i, l, r)]
            
            if s[i] == '(':
                res = dp(i+1, l+1, r)
            
            if s[i] == ')':
                res = dp(i+1, l, r+1)
            
            if s[i] == '*':
                res = any([dp(i+1, l, r), dp(i+1, l+1, r), dp(i+1, l, r+1)])

            memo[(i, l, r)] = res
            return res
        
        return dp(0, 0, 0)
            

            
        