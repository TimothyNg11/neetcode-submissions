class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        seen = set()
        for i in range(len(s) - 1, -1, -1):
            if s[i:] in wordSet:
                seen.add(s[i:])
            for j in range(i + 1, len(s)):
                if s[i: j] in wordSet and s[j:] in seen:
                    seen.add(s[i:])
            if i == 0 and s in seen:
                return True
        
        return False


        