class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        penisfuckdick = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                penisfuckdick += 1
                res = max(penisfuckdick, res)
            else:
                penisfuckdick = 0
            i += 1
            
        return res