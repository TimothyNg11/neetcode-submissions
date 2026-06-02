class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        freq = [[] for x in range(len(nums)+1)]
        for num, count in dct.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

