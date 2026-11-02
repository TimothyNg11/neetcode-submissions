class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, flag, canBuy):
            if i == len(prices):
                return 0
            if (i, flag, canBuy) in memo:
                return memo[(i, flag, canBuy)]
            
            if canBuy == 0:
                best = dp(i+1, 0, 1)
                memo[(i, flag, canBuy)] = best
                return best

            if flag == 0: # must buy
                best = max(-1 * prices[i] + dp(i+1, 1, 1), dp(i+1, 0, 1))
            
            if flag == 1: # must sell
                best = max(prices[i] + dp(i+1, 0, 0), dp(i+1, 1, 1))
            
            memo[(i, flag, canBuy)] = best
            return best
        
        return dp(0, 0, 1)
    
        