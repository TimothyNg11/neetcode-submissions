class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if a + stack[-1] < 0:
                    stack.pop()
                elif a + stack[-1] > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return list(stack)

        