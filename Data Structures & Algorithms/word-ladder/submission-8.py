class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.arr = []
        queue = deque()
        queue.append((beginWord, 0, {beginWord}))

        while queue:
            curr, count, seen = queue.popleft()
            if curr == endWord:
                return count + 1
            for word in wordList:
                diff = len([1 for char1, char2 in zip(curr, word) if char1 != char2])
                if diff == 1 and word not in seen:
                    seen.add(word)
                    queue.append((word, count + 1, seen))
        
        return 0
