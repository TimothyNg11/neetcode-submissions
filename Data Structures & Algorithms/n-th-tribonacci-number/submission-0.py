class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def Tn(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memo:
                return memo[n]
            
            num = Tn(n-1) + Tn(n-2) + Tn(n-3)
            memo[n] = num
            return num
        
        return Tn(n)
        