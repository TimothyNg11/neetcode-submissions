class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        left, right = 0, 0

        while right < len(nums):
            total = sum(nums[left:right+1])
            maxSum = max(maxSum, total)
            if total <= 0:
                left = right +1
            right += 1
        
        return maxSum
            