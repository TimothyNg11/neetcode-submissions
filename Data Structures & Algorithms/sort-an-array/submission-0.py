class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        neg_nums = [-1 * x for x in nums]
        heapq.heapify(neg_nums)
        sorted_arr = deque()
        while neg_nums:
            sorted_arr.appendleft(-heapq.heappop(neg_nums))
        
        return list(sorted_arr)