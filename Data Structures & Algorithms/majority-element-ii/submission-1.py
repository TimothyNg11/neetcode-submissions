class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        
        arr = []
        for key in dct:
            if dct[key] > len(nums) // 3:
                arr.append(key)
        
        return arr
        