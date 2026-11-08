class Solution:
    def trap(self, height: List[int]) -> int:
        # for each bar, its the min of its left max height and right max height minus its onw heihgt

        left = []
        for l, num in enumerate(height):
            if l == 0:
                left.append(num)
            else:
                left.append(max(left[-1], height[l]))
        
        right = []
        for r in range(len(height) - 1, -1, -1):
            if r == len(height) - 1:
                right.append(num)
            else:
                right.append(max(right[-1], height[r]))
        


        penis = right[::-1]
        total = 0
        for i, h in enumerate(height):
            total += (min(left[i], penis[i]) - h)
        
        return total

           