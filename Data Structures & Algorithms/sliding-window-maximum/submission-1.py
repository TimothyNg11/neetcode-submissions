class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for i in range(len(nums) - k + 1):
            arr.append(max(nums[i: i + k]))
        
        return arr
        