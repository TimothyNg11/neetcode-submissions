class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wd = WordDictionary()
        for word in words:
            wd.addWord(word)

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(i, j, node, path):
            ch = board[i][j]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            word = path + ch

            if nxt.endOfWord:
                result.append(word)
                nxt.endOfWord = False  # dedupe

            board[i][j] = '#'  # mark visited
            if i + 1 < rows and board[i+1][j] != '#':
                dfs(i+1, j, nxt, word)
            if i - 1 >= 0 and board[i-1][j] != '#':
                dfs(i-1, j, nxt, word)
            if j + 1 < cols and board[i][j+1] != '#':
                dfs(i, j+1, nxt, word)
            if j - 1 >= 0 and board[i][j-1] != '#':
                dfs(i, j-1, nxt, word)
            board[i][j] = ch  # unmark

            # prune leaf nodes that can no longer match anything
            if not nxt.children:
                del node.children[ch]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, wd.root, "")

        return result