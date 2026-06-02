class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        lst = sorted(dct.items(), key=lambda x: x[1], reverse = True)
        return [x[0] for x in lst[:k]]

