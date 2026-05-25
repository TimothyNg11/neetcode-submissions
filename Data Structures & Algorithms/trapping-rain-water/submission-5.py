class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0 for x in range(len(height))]
        rightMax = [0 for y in range(len(height))]

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[-1] = height[-1]
        for j in range(len(height) - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[j])

        total = 0
        for k, num in enumerate(height):
            total = total + min(leftMax[k], rightMax[k]) - num

        return total 

        