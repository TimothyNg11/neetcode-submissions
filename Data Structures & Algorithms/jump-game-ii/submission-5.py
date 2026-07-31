class Solution:
    def jump(self, nums: List[int]) -> int:
        total = 0
        i = 0
        if len(nums) == 1:
            return 0

        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return total + 1
            m = float('-inf')
            for j in range(i+1, i + nums[i] + 1):
                m = max(m, j + nums[j])
                if m == j + nums[j]:
                    idx = j
            i = idx
            total += 1

        
        return total