class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def append(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    append(curr)
                    curr.pop()

        append([])
        return res  