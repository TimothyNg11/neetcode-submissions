class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == target:
                    return True
        return False
        