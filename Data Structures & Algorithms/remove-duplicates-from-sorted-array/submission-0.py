class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            if l == r:
                r += 1
                continue
            
            if nums[r] == nums[l]:
                nums.pop(r)
            else:
                l += 1
                r += 1
        
        return len(nums)
        