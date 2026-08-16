class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        res = ''
        for char in s:
            if char == '(':
                res += char
                stack.append('(')
            elif char == ')':
                if not stack:
                    continue
                stack.pop()
                res += char
            else:
                res += char
        a = len(stack)
        for i in range(len(res) - 1, -1, -1):
            if a:
                if res[i] == '(':
                    res = res[:i] + res[i+1:]
                    a -= 1
        
        return res

        