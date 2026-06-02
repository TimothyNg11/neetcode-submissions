class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lst = sorted(intervals, key=lambda x: x[0])
        res = deque()
        res.append(lst[0])

        for start, end in lst[1:]:
            last = res[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                res.append([start, end])
        
        return list(res)