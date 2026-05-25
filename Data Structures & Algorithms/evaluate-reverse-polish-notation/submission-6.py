import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        dct = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda a,b: int(a/b)}
        for i, char in enumerate(tokens):
            if char not in dct:
                stack.append(int(char))
            else:
                b, a = stack.pop(), stack.pop()
                result = dct[char](a, b)
                stack.append(result)
        
        return stack[0]