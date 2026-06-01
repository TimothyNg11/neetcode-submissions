class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            minimum = min(nums[i:])
            idx = nums.index(minimum, i)
            temp = nums[i]
            nums[i] = minimum
            nums[idx] = temp


        