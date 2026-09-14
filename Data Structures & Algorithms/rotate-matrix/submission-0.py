class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # flip over the main diagonal
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i == j:
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
        # reverse the rows
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                end = len(matrix[0]) - 1
                if end - y <= y:
                    break
                temp = matrix[x][end - y]
                matrix[x][end - y] = matrix[x][y]
                matrix[x][y] = temp
        