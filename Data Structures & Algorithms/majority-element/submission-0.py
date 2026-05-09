class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] > len(nums) / 2:
                return num
        return num