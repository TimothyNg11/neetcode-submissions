class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 1
        curr = s[0] if s else ''
        counter = 1
        count = 1
        for i in range(1, len(s) - 1):
            while counter < len(s) and s[i-counter: i+counter+1] == s[i-counter: i+counter+1][::-1]:
                substr = s[i-counter: i+counter+1]
                maxL = max(maxL, len(substr))
                if maxL == len(substr):
                    curr = substr
                counter += 1
            counter = 1
        
        for j in range(1, len(s)):
            while count < len(s) and s[j-count: j+count] == s[j-count: j+count][::-1]:
                substr = s[j-count: j+count]
                maxL = max(maxL, len(substr))
                if maxL == len(substr):
                    curr = substr
                count += 1
            count = 1

        return curr

        