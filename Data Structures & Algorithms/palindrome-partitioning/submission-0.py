class Solution:
    def partition(self, s: str) -> List[List[str]]:
        fin = []
        def backtrack(string, res):
            if "".join(res) == s:
                fin.append(res[:])
                return
            for i, char in enumerate(string):
                if string[:i+1] == string[:i+1][::-1]:
                    res.append(string[:i+1])
                    backtrack(string[i+1:], res)
                    res.pop()
            
            return
        
        backtrack(s, [])
        return fin

        