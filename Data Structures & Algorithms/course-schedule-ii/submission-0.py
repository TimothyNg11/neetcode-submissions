class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]

        for courses in prerequisites:
            course, preq = courses[0], courses[1]
            adjList[preq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i, num in enumerate(indegree):
            if num == 0:
                queue.append(i)
        res = []
        counter = 0
        while queue:
            node = queue.popleft()
            for c in adjList[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
            res.append(node)
            counter += 1
        
        if counter != numCourses:
            return []
        return res
        