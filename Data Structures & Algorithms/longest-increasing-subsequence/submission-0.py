class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def choose(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            best = choose(i+1, prev) # skip

            if prev == -1 or nums[i] > nums[prev]:
                best = max(best, 1 + choose(i+1, i))
            
            memo[(i, prev)] = best
            return best
        
        return choose(0, -1)
            

        