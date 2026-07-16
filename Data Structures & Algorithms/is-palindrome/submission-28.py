class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ''
        for char in s:
            if char.isalnum():
                string += char
        
        return string == string[::-1]