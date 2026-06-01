class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        cur = 0

        for num in nums:
            cur = max(cur, 0)
            cur += num
            maxsum = max(maxsum, cur)
        
        return maxsum