class Solution:

    def __init__(self, w: List[int]):
        self.lst = w
        

    def pickIndex(self) -> int:
        a = sum(self.lst)
        b = random.random() *a 
        total = 0
        for i in range(len(self.lst)):
            total += self.lst[i]
            if total > b:
                return i



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()