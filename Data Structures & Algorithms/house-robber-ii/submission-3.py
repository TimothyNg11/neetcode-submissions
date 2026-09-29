class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = {}
        memo2 = {}

        def dfs(i, flag):
            if i >= len(nums):
                return 0
            if not flag and i in memo1:
                return memo1[i]
            if flag and i in memo2:
                return memo2[i]

            if i == 0:
                best = max(dfs(i+1, 0), nums[i] + dfs(i+2, 1))
            else:
                if flag:
                    if i == len(nums) - 1:
                        return 0
                best = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag))
            if not flag:
                memo1[i] = best
            else:
                memo2[i] = best
            return best
        
        return dfs(0, 0)
        