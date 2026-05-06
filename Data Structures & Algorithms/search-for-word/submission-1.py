class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, count):
            if count == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[count]:
                return False
            
            temp = board[i][j]
            board[i][j] = "@"

            res = dfs(i+1, j, count + 1) or dfs(i-1, j, count+1) or dfs(i, j+1, count+1) or dfs(i, j-1, count + 1)
            board[i][j] = temp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
