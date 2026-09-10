class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = int((len(nums) + 1) * (len(nums)) / 2)
        return a - sum(nums)