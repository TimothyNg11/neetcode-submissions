class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        i, j = 0, 0

        while i < len(prices) and j < len(prices):
            diff = max(diff, prices[j]-prices[i])
            if prices[j] <= prices[i]:
                i = j
                j += 1
            else:
                j += 1

        return diff