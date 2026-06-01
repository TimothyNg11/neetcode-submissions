class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for x in range(len(nums))]

        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dp(i+1), nums[i] + dp(i+2))
            return memo[i]

        return dp(0)