class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque([amount])
        visited = [amount]
        counter = 0

        while queue:
            counter += 1
            for i in range(len(queue)):
                key = queue.popleft()
                for coin in coins:
                    if key - coin == 0:
                        return counter
                    if key - coin > 0 and key - coin not in visited:
                        visited.append(key - coin)
                        queue.append(key - coin)
        
        return -1

        