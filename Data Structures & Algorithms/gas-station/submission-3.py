class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, idx = 0, 0
        if sum(gas) < sum(cost):
            return -1
        
        for i, num in enumerate(gas):
            total += gas[i] - cost[i]
            if total < 0:
                idx = i + 1
                total = 0
        
        return idx
