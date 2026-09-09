class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        count = 0
        for i in range(n+1):
            num = bin(i)[2:]
            for char in num:
                if char == '1':
                    count += 1
            res.append(count)
            count = 0
        
        return res
        