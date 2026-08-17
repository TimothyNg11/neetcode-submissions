class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        for i, char in enumerate(s):
            total += 1
            x, y = i - 1, i + 1
            while x >= 0 and y < len(s):
                if s[x] == s[y]:
                    total += 1
                    x -= 1
                    y += 1
                else:
                    break
        
        for j in range(1, len(s)):
            if s[j-1] == s[j]:
                total += 1
                a, b = j - 2, j + 1
                while a >= 0 and b < len(s):
                    if s[a] == s[b]:
                        total += 1
                        a -= 1
                        b += 1
                    else:
                        break

        return total
