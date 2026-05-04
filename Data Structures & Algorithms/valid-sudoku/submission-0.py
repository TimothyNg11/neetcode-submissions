class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(grid):
            dct = {}
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    num = grid[i][j]
                    if num != "." and num not in dct:
                        dct[num] = -1
                    elif num in dct:
                        return False
                dct.clear()
            return True
        
        def checkCols(grid):
            dct = {}
            for j in range(len(grid[0])):
                for i in range(len(grid)):
                    num = grid[i][j]
                    if num != "." and num not in dct:
                        dct[num] = -1
                    elif num in dct:
                        return False
                dct.clear()
            return True
        
        def checkBoxes(grid):
            dct = {}
            for x in [0, 3, 6]:
                for y in [0, 3, 6]:
                    for i in range(3):
                        for j in range(3):
                            num = grid[x+i][y+j]
                            if num != "." and num not in dct:
                                dct[num] = -1
                            elif num in dct:
                                return False
                    dct.clear()
            return True
        
        return checkRows(board) and checkCols(board) and checkBoxes(board)
        

        