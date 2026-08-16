class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        a = 0
        l = 0
        for i, r in enumerate(s):
            dct[r] = dct.get(r, 0) + 1
            while dct[r] >= 2:
                dct[s[l]] = dct[s[l]] - 1
                l += 1
            a = max(a, i - l + 1)
        
        return a
            

        