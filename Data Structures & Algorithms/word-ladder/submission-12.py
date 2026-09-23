class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = {word : [] for word in wordList}
        adjList[beginWord] = []
        def compare(w1, w2):
            x = 0
            count = 0
            while x < len(w1):
                if w1[x] != w2[x]:
                    count += 1
                x += 1
            
            return count == 1
        for i in range(len(wordList)):
            if compare(beginWord, wordList[i]):
                adjList[beginWord].append(wordList[i])
                adjList[wordList[i]].append(beginWord)

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if compare(wordList[i], wordList[j]):
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        
        queue = deque()
        queue.append((beginWord, 0))
        seen = set()
        while queue:
            word, curr = queue.popleft()
            seen.add(word)
            if word == endWord:
                return curr + 1
            for c in adjList[word]:
                if c not in seen:
                    queue.append((c, curr + 1))
        
        return 0

