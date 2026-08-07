class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string = string + str(digit)
        
        return list(str(int(string) + 1))

        