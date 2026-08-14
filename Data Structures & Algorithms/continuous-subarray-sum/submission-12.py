class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool: 
        dct = {0: [-1]}
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total % k in dct:
                for val in dct[total % k]:
                    if i - val > 1:
                        return True
            if total % k not in dct:
                dct[total % k] = []
            dct[total % k].append(i)
        
        return False
            
             