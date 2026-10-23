class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        def append(curr, lst):
            if len(lst) == len(nums):
                res.append(lst[:])
                return
            for num in dct:
                if num not in curr or curr[num] < dct[num]:
                    curr[num] = curr.get(num, 0) + 1
                    lst.append(num)
                    append(curr, lst)
                    lst.pop()
                    curr[num] -= 1
        
        append({}, [])
        return res

        