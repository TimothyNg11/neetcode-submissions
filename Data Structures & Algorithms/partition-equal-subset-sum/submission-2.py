class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(sum1, sum2, i):
            if sum1 == sum2 and i == len(nums):
                return True
            if i == len(nums):
                return False
            if (sum1, sum2, i) in memo:
                return memo[(sum1, sum2, i)]
            best = dfs(sum1+nums[i], sum2, i+1) or dfs(sum1, sum2+nums[i], i+1)
            memo[(sum1, sum2, i)] = best
            return best
        
        return dfs(0, 0, 0)