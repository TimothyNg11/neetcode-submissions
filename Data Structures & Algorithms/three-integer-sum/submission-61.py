class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 1, len(nums) - 1
        res = []
        sett = set()

        for i, num in enumerate(nums):
            while l < r:
                curr = num + nums[l] + nums[r] # num + nums[l] + nums[r] = 0
                if curr == 0:
                    if (num, nums[l], nums[r]) not in sett:
                        res.append([num, nums[l], nums[r]])
                        sett.add((num, nums[l], nums[r]))
                        
                    l += 1
                    r -= 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
            l = i + 2
            r = len(nums) - 1
        
        return res
        
        # [-4, -1, -1, 0, 1, 2]






            
            
