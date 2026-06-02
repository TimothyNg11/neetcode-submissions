class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for x in range(len(nums))]
        memo2 = [-1 for x in range(len(nums))]

        if len(nums) == 1:
            return nums[0]

        def dp(i, flag):
            if flag and i >= len(nums) - 1:
                return 0
            if not flag and i >= len(nums):
                return 0
            if flag and memo[i] != -1:
                return memo[i]
            if not flag and memo2[i] != -1:
                return memo2[i]
            
            if flag:
                memo[i] = max(dp(i+1, True), nums[i] + dp(i+2, True))
                return memo[i]
            else:
                memo2[i] = max(dp(i+1, False), nums[i] + dp(i+2, False))
                return memo2[i]

        return max(dp(0, True), dp(1, False))
        