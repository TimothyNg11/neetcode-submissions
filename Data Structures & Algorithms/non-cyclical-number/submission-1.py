class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            total = 0
            for char in str(n):
                total += int(char)**2
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total
        