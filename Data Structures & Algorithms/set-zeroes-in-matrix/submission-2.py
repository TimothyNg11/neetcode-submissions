class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xc, yc = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    xc.add(i)
                    yc.add(j)
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in xc or y in yc:
                    matrix[x][y] = 0
                            
        
        