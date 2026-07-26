class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res = res + [x + [num] for x in res]
        
        dct = {}
        for subset in res:
            dct[tuple(sorted(subset))] = 1
        
        return list(dct.keys())
     