class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount+1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and memo[i-coin] != float('inf'):
                    memo[i] = min(memo[i], memo[i - coin] + 1)
        
        return memo[amount] if memo[amount] != float('inf') else -1

        