class Solution:
    def numSquares(self, n: int) -> int:
        dct = {}
        i = 1
        while i * i <= n:
            dct[i*i] = i
            i += 1
        memo = {0: 0, 1: 1}
        queue = deque()
        queue.append(0)
        seen = set()
        while queue:
            num = queue.popleft()
            if num == n:
                return memo[num]
            for square in dct:
                if num + square > n:
                    break
                memo[num + square] = min(memo.get(num + square, float('inf')), memo[num] + 1)
                if num + square not in seen:
                    queue.append(num + square)
                seen.add(num + square)

        return memo[n]


        