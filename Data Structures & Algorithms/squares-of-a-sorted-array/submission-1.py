class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        arr = []
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                arr.insert(0, nums[i] * nums[i])
                i = i + 1
            else:
                arr.insert(0, nums[j] * nums[j])
                j = j - 1
        
        return arr
