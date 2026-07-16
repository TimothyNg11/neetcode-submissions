class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        arr = [0] * len(nums)
        counter = -1
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                arr[counter] = nums[i] * nums[i]
                i = i + 1
            else:
                arr[counter] = nums[j] * nums[j]
                j = j - 1
            counter -= 1 
        
        return arr
