class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    queue.append((i, j))
                    board[i][j] = 'T'

        while queue:
            x, y = queue.popleft()
            board[x][y] = 'T'
            for rx, ry in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + rx, y + ry
                if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]):
                    if board[nx][ny] == 'O':
                        queue.append((nx, ny))

        for a in range(len(board)):
            for b in range(len(board[0])):
                if board[a][b] == 'O':
                    board[a][b] = 'X'
                if board[a][b] == 'T':
                    board[a][b] = 'O' 

                
        