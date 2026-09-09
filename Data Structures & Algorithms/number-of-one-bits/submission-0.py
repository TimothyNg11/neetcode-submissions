class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:]
        count = 0
        for char in num:
            if char == '1':
                count += 1
        
        return count