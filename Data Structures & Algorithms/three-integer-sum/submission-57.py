class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, mid, right = 0, 1, len(nums) - 1
        arr = set()

        while left < len(nums) - 2:
            while mid < right:
                total = nums[left] + nums[right] + nums[mid]
                if total == 0:
                    arr.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1
                if total < 0:
                    mid += 1
                if total > 0:
                    right -= 1
            left += 1
            mid = left + 1
            right = len(nums) - 1
        
        lst = []
        for triple in arr:
            lst.append(list(triple))
        
        return lst
            
            
