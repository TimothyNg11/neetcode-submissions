class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = []
        self.dct[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        
        l, r = 0, len(self.dct[key]) - 1
        curr_max = -1
        res = ''
        while l <= r:
            m = l + (r - l) // 2
            if self.dct[key][m][0] == timestamp:
                return self.dct[key][m][1]
            if self.dct[key][m][0] <= timestamp:
                curr_max = max(curr_max, self.dct[key][m][0])
                if curr_max == self.dct[key][m][0]:
                    res = self.dct[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
    
