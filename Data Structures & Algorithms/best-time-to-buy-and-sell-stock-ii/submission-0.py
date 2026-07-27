class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        l, r = 0, 0

        while l < len(prices) and r < len(prices):
            res = prices[r] - prices[l]
            if res > 0:
                diff += res
                l = r
                r += 1
            else:
                l = r
                r += 1
        
        return diff
        