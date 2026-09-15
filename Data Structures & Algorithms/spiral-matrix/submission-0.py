class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        counter = 0
        
        while top <= bottom and left <= right:
            if counter % 4 == 0:            # go left to right
                for y in range(left, right + 1):
                    arr.append(matrix[top][y])
                top += 1
            
            if counter % 4 == 1:            # go up to down
                for x in range(top, bottom + 1):
                    arr.append(matrix[x][right])
                right -= 1
            
            if counter % 4 == 2:            # go right to left
                for y in range(right, left - 1, -1):
                    arr.append(matrix[bottom][y])
                bottom -= 1
            
            if counter % 4 == 3:           # go down to up
                for x in range(bottom, top - 1, -1):
                    arr.append(matrix[x][left])
                left += 1
            
            counter += 1
        
        return arr
        