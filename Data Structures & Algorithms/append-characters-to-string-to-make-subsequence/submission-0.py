class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        for char in s:
            if l == len(t):
                return 0
            if char == t[l]:
                l += 1
        
        return len(t) - l
            
        