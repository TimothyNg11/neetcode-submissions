class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        dct = {}
        for task in tasks:
            dct[task] = dct.get(task, 0) + 1
        
        queue = [-x for x in dct.values()]
        heapq.heapify(queue)
        cooldown = deque()

        while queue or cooldown:
            if queue:
                a = heapq.heappop(queue)
                if -a - 1 > 0:
                    cooldown.append((time + n, -a - 1))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(queue, -cooldown[0][1])
                cooldown.popleft()
            time += 1

        return time
        