class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)
        for n in range(2, len(cost) + 1):
            memo[n] = min(memo[n-1] + cost[n-1], memo[n-2] + cost[n-2])
        
        return memo[len(cost)]
            
        
        