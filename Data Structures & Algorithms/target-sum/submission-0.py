class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        counter = 0
        def dp(total, i):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            if ((total, i)) in memo:
                return memo[(total, i)]
        
            best = dp(total + nums[i], i + 1) + dp(total - nums[i], i + 1)
            memo[(total, i)] = best
            return best
        
        return dp(0, 0)


        