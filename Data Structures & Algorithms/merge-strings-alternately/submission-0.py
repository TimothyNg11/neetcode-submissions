class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        string = ""
        i = 0
        j = 0
        while word1[i:] and word2[j:]:
            if counter % 2 == 0:
                string = string + word1[i]
                i = i + 1
            else:
                string = string + word2[j]
                j = j + 1
            counter += 1
        
        if word1[i:]:
            string = string + word1[i:]
        else:
            string = string + word2[j:]
        return string

        