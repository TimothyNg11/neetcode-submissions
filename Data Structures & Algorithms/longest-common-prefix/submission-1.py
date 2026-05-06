class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dct = {}
        minLen = min([len(x) for x in strs])
        res = ''

        for j in range(minLen):
            for i, string in enumerate(strs):
                if string[j] not in dct:
                    dct[string[j]] = dct.get(string[j], 0) + 1
                else:
                    dct[string[j]] = dct.get(string[j], 0) + 1
            if dct[string[j]] == len(strs):
                dct.clear()
                res = res + string[j]
            else:
                return res
        return res

