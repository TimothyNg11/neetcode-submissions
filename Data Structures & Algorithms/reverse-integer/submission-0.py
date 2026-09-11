class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1:
            return 0
        a = str(x)[::-1]
        if a[-1] == '-':
            a = '-' + a[:len(a) - 1]
        
        b = int(a)
        if b < -1 * 2**31 or b > 2**31 - 1:
            return 0
        return b
        