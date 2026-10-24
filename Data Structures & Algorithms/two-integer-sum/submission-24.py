class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            if num not in dct:
                dct[num] = []
            dct[num].append(i)

        nums.sort()
        l, r = 0, len(nums) - 1


        while l < r:
            curr = nums[l] + nums[r]
            if curr == target:
                if len(dct[nums[l]]) == 2:
                    return sorted(dct[nums[l]])
                else:
                    return sorted(dct[nums[l]] + dct[nums[r]])
            if curr > target:
                r -= 1
            else:
                l += 1
        