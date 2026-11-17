class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # map each letter to its [first, last] index (dict keeps first-seen order)
        intervals = {}
        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i]
            intervals[char][1] = i

        # merge overlapping intervals (already sorted by start)
        merged = []
        for start, end in intervals.values():
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return [end - start + 1 for start, end in merged]