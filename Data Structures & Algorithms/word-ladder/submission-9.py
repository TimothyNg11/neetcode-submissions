class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        a = set(wordList)
        queue = deque()
        queue.append((beginWord, 0, {beginWord}))

        while queue:
            curr, count, seen = queue.popleft()
            if curr == endWord:
                return count + 1
            for i in range(len(curr)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    word = curr[:i] + char + curr[i+1:]
                    if word in a and word not in seen:
                        seen.add(word)
                        queue.append((word, count + 1, seen))
        
        return 0
