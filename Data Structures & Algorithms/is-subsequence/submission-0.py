class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        for char in t:
            if ps == len(s):
                return True
            if char == s[ps]:
                ps += 1
        if ps == len(s):
            return True
        return False