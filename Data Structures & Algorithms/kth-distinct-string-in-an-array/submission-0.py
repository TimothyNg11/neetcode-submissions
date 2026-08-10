class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dct = {}
        for string in arr:
            dct[string] = dct.get(string, 0) + 1
        
        i = 0
        for milan in arr:
            if dct[milan] == 1:
                i += 1
            if i == k:
                return milan

        return ""