class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(math.ceil(p / k) for p in piles)

        def binarySearch(left, right):
            k = left + (right - left) // 2
            counter = 0

            if right == left + 1 or right == left - 1:
                return right

            if hours_needed(k) > h:
                return binarySearch(k, right)
            
            return binarySearch(left, k)
        
        return binarySearch(0, max(piles))





        