class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            if num in dct:
                return num
            dct[num] = 1