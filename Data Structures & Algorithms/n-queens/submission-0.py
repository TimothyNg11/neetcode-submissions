class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        seen = set()
        self.res = []
        def dfs(queens, row, count):
            if count == n:
                arr = []
                for x, y in queens:
                    string = ''
                    for i in range(n):
                        if y == i:
                            string += 'Q'
                        else:
                            string += '.'
                    arr.append(string)
                self.res.append(arr)               # dedup check no longer needed
                return

            for j in range(n):
                if (row, j) not in seen:
                    lst = []
                    for a in range(n):
                        lst.append((row, a))
                        lst.append((a, j))
                    counter = 1
                    while row + counter < n and j + counter < n:      # FIX 1
                        lst.append((row + counter, j + counter))
                        counter += 1
                    counter2 = 1
                    while j - counter2 >= 0 and row + counter2 < n:
                        lst.append((row + counter2, j - counter2))    # FIX 2
                        counter2 += 1
                    lst = [l for l in lst if l not in seen]           # FIX 3
                    for l in lst:
                        seen.add(l)
                    queens.append((row, j))
                    dfs(queens, row + 1, count + 1)
                    queens.pop()
                    for l in lst:
                        seen.discard(l)
            return

        dfs([], 0, 0)
        return self.res