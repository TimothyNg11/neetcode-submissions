class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices of bars in increasing height order
        max_area = 0
        for i, h in enumerate(heights + [0]):  # sentinel flushes the stack
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area



        