class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # graph cycle detection
        # map characers -> ones that come after it
        # use kahns alg if there is a cycle then return ''
        # else return valid topo sort
        adjList = {}
        inDegree = {}
        seen = set()
        if len(words) == 1:
            return words[0]
        for i in range(1, len(words)):
            first, second = words[i-1], words[i]
            for char in first:
                seen.add(char)
                if char not in adjList:
                    adjList[char] = set()
                    inDegree[char] = 0
            for c in second:
                seen.add(c)
                if c not in adjList:
                    adjList[c] = set()
                    inDegree[c] = 0
            j, length = 0, min(len(first), len(second))
            while j < length:
                if first[j] == second[j]:
                    if j == length - 1 and len(first) > len(second):
                        return ''
                    j += 1
                    continue
                else:

                    if second[j] not in adjList[first[j]]:
                        inDegree[second[j]] = inDegree.get(second[j], 0) + 1
                    adjList[first[j]].add(second[j])
                    break
        
        total = len(seen)
        
        queue = deque()
        for char in inDegree:
            if not inDegree[char]:
                queue.append(char)
        
        arr = []
        counter = 0
        while queue:
            char = queue.popleft()
            arr.append(char)
            for child in adjList[char]:
                inDegree[child] -= 1
                if not inDegree[child]:
                    queue.append(child)
            counter += 1
        
        if counter != total:
            return ''
        return str(''.join(arr))
        


                
        